CREATE TABLE `spider_pool` (
  `pool_id` smallint(10) NOT NULL AUTO_INCREMENT,
  `spider_type` smallint(10) NOT NULL,
  `identify` char(100) NOT NULL,
  `published_at` bigint(20) DEFAULT NULL,
  `follow_num` smallint(10) DEFAULT NULL,
  PRIMARY KEY (`pool_id`),
  index `spider_pool_identify_index` (`identify`),
  index `spider_pool_pool_id_index` (`pool_id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;

CREATE TABLE `user` (
  `user_id` smallint(10) NOT NULL AUTO_INCREMENT,
  `user_identify` varchar(100) DEFAULT NULL,
  `nickname` varchar(100) NOT NULL,
  `published_at` bigint(20) DEFAULT NULL,
  `description` varchar(100) DEFAULT NULL,
  `avatar` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`user_id`),
  index `user_user_id_index` (`user_id`),
  index `user_user_identify_index` (`user_identify`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;

CREATE TABLE `user_spider_pool` (
  `id` smallint(10) NOT NULL AUTO_INCREMENT,
  `user_id` smallint(10) NOT NULL,
  `pool_id` smallint(10) NOT NULL,
  `published_at` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  index `user_spider_pool_user_id_index` (`user_id`),
  index `user_spider_pool_pool_id_index` (`pool_id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;

CREATE TABLE `jianshu_topic_feed` (
  `id` smallint(10) NOT NULL AUTO_INCREMENT,
  `user_id` smallint(10) NOT NULL,
  `pool_id` smallint(10) NOT NULL,
  `topic_identify` varchar(100) NOT NULL,
  `title` varchar(500) DEFAULT NULL,
  `summary` varchar(500) DEFAULT NULL,
  `published_at` bigint(20) NOT NULL,
  `inserted_at` bigint(20) NOT NULL,

  PRIMARY KEY (`id`),
  index `jianshu_topic_feed_user_id_index` (`user_id`),
  index `jianshu_topic_feed_published_at_index` (`published_at` desc),
  index `jianshu_topic_feed_inserted_at_index` (`inserted_at` desc),
  index `jianshu_topic_feed_topic_identify_index` (`topic_identify`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;