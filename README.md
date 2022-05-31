# QueryRDFlessurligneurs
Pass the query as an argument to the file queryData.py

For example to query the lessurligneurs that containes a list of entities "Entity1 Entity2 Entity3" you should write: python queryData.py "Entity1 Entity2 Entity3"
If the entity consists of more than one word for example (Emmanuel Macron) you sould replace the space with (-), then the entity will be (Emmanuel-Macron)
The result will be the titles for all the surligneurs containing the entities in our query.


For example if we write: python queryData.py "Emmanuel-Macron Parlement"

The result is:

============QUERY RESULTS===============

We Have 7 results
The results are:
Projet de loi climat  un engagement minimum de la France au regard des objectifs européens

Le ministre des finances Bruno Le Maire pourrait revenir sur la suppression de la taxe dhabitation pour les 20  des ménages les plus aisés. Que dira le Conseil constitutionnel

Les partis politiques européens  que sont-ils et à quoi servent-ils

Spitzenkandidat  Comment sera désigné le Président de la Commission en 2019

Rejet de la candidature de Sylvie Goulard par le Parlement européen. Pour Amélie de Montchalin  cest une crise institutionnelle majeure pour lEurope

Danemark  déplacer les demandes dasile vers un autre pays juridiquement possible

Jean-Luc Mélenchon sur la discipline de vote des députés La France insoumise  Celles et ceux qui accepteront cette investiture sengagent à  respecter la discipline de vote
