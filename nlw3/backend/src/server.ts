import express from 'express';
import path from 'path';
import cors from 'cors';


import 'express-async-errors';

import './database/connection';

import routes from './routes';
import errorHandler from './errors/handler'

const app = express();

app.use(cors());
app.use(express.json());

// Rota = conjunto
// Recurso = usuário

// Métodos HTTP = GET, POST, PUT, DELETE
// Parmetros :

// query: http://localhost:3333/users?search=nome
// Route: http://localhost:3333/users/1 (identificar um recurso)
// Body: http://localhost:3333/users

app.use(routes);
app.use('/uploads', express.static(path.join(__dirname, '..', 'uploads')));
app.use(errorHandler);

app.listen(3333);

