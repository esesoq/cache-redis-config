// types.ts

import { RedisClusterOptions } from 'ioredis';

export interface CacheRedisConfig {
  host: string;
  port: number;
  password?: string;
  db?: number;
  prefix?: string;
}

export interface CacheRedisOptions {
  cluster?: RedisClusterOptions;
  single?: RedisClusterOptions;
}

export type CacheRedisConfigType = CacheRedisConfig & CacheRedisOptions;