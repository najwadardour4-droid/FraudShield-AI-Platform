export const MOCK_USERS = [
  { id:1, name:'Alice Benali',  email:'alice@corp.ma', role:'user',  avatar:'AB', active:true  },
  { id:2, name:'Bob Karimi',    email:'bob@corp.ma',   role:'user',  avatar:'BK', active:true  },
  { id:3, name:'Carol Tazi',    email:'carol@corp.ma', role:'user',  avatar:'CT', active:false },
  { id:4, name:'Admin Système', email:'admin@invoiceguard.ai', role:'admin', avatar:'AS', active:true  },
];

export const MOCK_INVOICES = [
  { id:'FACT-2026-00891', vendor:'BTP Maroc SARL',  date:'14/05/2026', amount:18400, score:94, status:'fraud',   user:'alice@corp.ma',  features:['Sceau absent','TVA altérée','Police incohérente'] },
  { id:'FACT-2026-00834', vendor:'LogiTech Pro',    date:'09/05/2026', amount:7250,  score:87, status:'fraud',   user:'bob@corp.ma',    features:['Montant retouché','Logo copié'] },
  { id:'FACT-2026-00812', vendor:'Fournitech SARL', date:'07/05/2026', amount:3100,  score:71, status:'suspect', user:'alice@corp.ma',  features:['Signature manquante'] },
  { id:'FACT-2026-00798', vendor:'Espace Bureau',   date:'03/05/2026', amount:9870,  score:63, status:'suspect', user:'carol@corp.ma',  features:['Alignement suspect'] },
  { id:'FACT-2026-00774', vendor:'MediaPrint Co',   date:'01/05/2026', amount:1440,  score:12, status:'normal',  user:'bob@corp.ma',    features:[] },
  { id:'FACT-2026-00761', vendor:'Agence Atlas',    date:'28/04/2026', amount:550,   score:8,  status:'normal',  user:'carol@corp.ma',  features:[] },
];

export const MONTHLY = [
  {m:'Nov',anomalies:98, fraud:14},
  {m:'Déc',anomalies:112,fraud:18},
  {m:'Jan',anomalies:142,fraud:22},
  {m:'Fév',anomalies:158,fraud:26},
  {m:'Mar',anomalies:171,fraud:29},
  {m:'Avr',anomalies:189,fraud:33},
  {m:'Mai',anomalies:214,fraud:38},
];
