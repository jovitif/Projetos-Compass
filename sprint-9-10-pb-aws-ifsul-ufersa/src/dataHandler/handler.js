import serverless from 'serverless-http';
import app from './animalRouter';

export const handler = serverless(app);
