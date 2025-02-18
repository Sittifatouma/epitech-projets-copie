# Back end

Use docker-compose to launch the application


```bash
docker-compose up -d
```

To launch manually, make sure that you pointed on the right database.
Modify this line if needed:

```bash
//  dataSource.setUrl("jdbc:mysql://localhost:3306/sharntDB");
```

then use, after making sure that maven is well install

```bash
mvn clean
mvn install
mvn spring-boot:run
```