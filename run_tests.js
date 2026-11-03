// Run: node tests/run_tests.js   (Node 16+, no dependencies)
const fs=require("fs"),path=require("path"),vm=require("vm");
const html=fs.readFileSync(path.join(__dirname,"..","index.html"),"utf8");
const code=html.match(/<script>([\s\S]*?)<\/script>/)[1]; // first block = DOM-free engine + synthetic cases
const ctx={};vm.createContext(ctx);vm.runInContext(code+";this.ENGINE=ENGINE;this.CASES=CASES;",ctx);
const {ENGINE,CASES}=ctx;let fail=0,n=0;
const ok=(c,m)=>{n++;if(!c){fail++;console.log("FAIL:",m)}};
const RATE=0.08;
// independent closed-form check: annuity-due, zero escalation, 12 months at 8% p.a.
const m=Math.pow(1+RATE,1/12)-1,annDue=2000*(1-Math.pow(1+m,-12))/m*(1+m);
ok(Math.abs(ENGINE.pv(12,2000,0,RATE)-annDue)<1e-6,"PV matches annuity-due formula");
ok(Math.abs(ENGINE.pv(12,2000,0,RATE)-23173.863853)<1e-5,"PV matches independently computed reference 23173.863853");
for(const c of CASES){
  const r=ENGINE.run(c,RATE);
  ok(r.status===c.exp,`${c.id}: status ${r.status} != expected ${c.exp}`);
  if(r.status==="BLOCKED")ok(r.liability===null,`${c.id}: blocked case was calculated`);
  for(const f of ["term","rent","esc"]){const v=r.fields[f].value;if(v!=null)ok(v===c.truth[f],`${c.id}: accepted wrong ${f}=${v}`)}
}
ok(ENGINE.verify({field:"term",value:60,quote:"text not in the document"},"abc").st==="rejected","fabricated quote rejected");
ok(ENGINE.verify({field:"rent",value:50000,quote:"Rent is $5,000 per month"},"Rent is $5,000 per month").st==="rejected","value not supported by quote rejected");
const E=ENGINE.evaluate(RATE,CASES);
ok(E.pipe.wrong===0,"pipeline accepted no wrong values");
console.log(`${n} checks, ${fail} failed. Baseline status ${E.base.status}/12, pipeline status ${E.pipe.status}/12.`);
process.exit(fail?1:0);
