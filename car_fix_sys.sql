/*
 Navicat Premium Data Transfer

 Source Server         : 2048game
 Source Server Type    : MySQL
 Source Server Version : 80027
 Source Host           : localhost:3306
 Source Schema         : car_fix_sys

 Target Server Type    : MySQL
 Target Server Version : 80027
 File Encoding         : 65001

 Date: 01/08/2022 13:23:25
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for administration
-- ----------------------------
DROP TABLE IF EXISTS `administration`;
CREATE TABLE `administration`  (
  `Administration_num` int NOT NULL AUTO_INCREMENT,
  `Administration_name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `Administration_money` int NULL DEFAULT NULL,
  `Administration_password` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `Administration_fix_num` int NULL DEFAULT NULL,
  PRIMARY KEY (`Administration_num`) USING BTREE,
  INDEX `Administration_name`(`Administration_name`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1026 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of administration
-- ----------------------------
INSERT INTO `administration` VALUES (1000, 'SONG', 1234, '123456', 53);
INSERT INTO `administration` VALUES (1001, 'QI', 10000, '123456', 100);
INSERT INTO `administration` VALUES (1003, 'BIN', 1000, '123456', 60);
INSERT INTO `administration` VALUES (1004, '小宋', 10000, '123456', 42);
INSERT INTO `administration` VALUES (1005, '小琦', 1200, '123465', 45);
INSERT INTO `administration` VALUES (1006, '小斌', 4156, '21313', 45);
INSERT INTO `administration` VALUES (1007, '小张', 4567, '23145', 89);
INSERT INTO `administration` VALUES (1008, '小明', 43456, '12313', 89);
INSERT INTO `administration` VALUES (1009, '小号', 566, '134566', 63);
INSERT INTO `administration` VALUES (1011, '华为', 12, '4555', 89);
INSERT INTO `administration` VALUES (1012, '小米', 4000, '1223465', 85);
INSERT INTO `administration` VALUES (1013, 'oppo', 600, '78994', 98);
INSERT INTO `administration` VALUES (1022, '大宋', 456, '123456', 80);
INSERT INTO `administration` VALUES (1024, '大博', 4000, '123456', 89);
INSERT INTO `administration` VALUES (1025, '大琦', 5000, '15465', 89);

-- ----------------------------
-- Table structure for car_master
-- ----------------------------
DROP TABLE IF EXISTS `car_master`;
CREATE TABLE `car_master`  (
  `car_master_num` int NOT NULL AUTO_INCREMENT,
  `car_master_name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `car_master_phnum` int NULL DEFAULT NULL,
  `car_master_cartype` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `car_master_user` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`car_master_num`) USING BTREE,
  INDEX `Administration_name`(`car_master_name`) USING BTREE,
  INDEX `car_master_user`(`car_master_user`) USING BTREE,
  CONSTRAINT `car_master_ibfk_1` FOREIGN KEY (`car_master_user`) REFERENCES `administration` (`Administration_name`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1043 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of car_master
-- ----------------------------
INSERT INTO `car_master` VALUES (1001, '小A', 10086, '奔驰', 'SONG');
INSERT INTO `car_master` VALUES (1022, '小B', 10087, '宝马', 'SONG');
INSERT INTO `car_master` VALUES (1023, '小C', 10088, '法拉利', 'SONG');
INSERT INTO `car_master` VALUES (1024, '小D', 10089, '特斯拉', 'SONG');
INSERT INTO `car_master` VALUES (1025, '小E', 10010, '特斯拉', '小宋');
INSERT INTO `car_master` VALUES (1027, '小F', 10011, '特斯拉', '小琦');
INSERT INTO `car_master` VALUES (1028, '大A', 10012, '五菱宏光', '小斌');
INSERT INTO `car_master` VALUES (1029, '大B', 10012, '三菱', '小斌');
INSERT INTO `car_master` VALUES (1030, '大C', 10013, '奥迪', '小琦');
INSERT INTO `car_master` VALUES (1031, '大E', 10014, '天启', '小斌');
INSERT INTO `car_master` VALUES (1032, '大F', 10015, '剃刀', '小琦');
INSERT INTO `car_master` VALUES (1033, '大G', 10016, '大Q吧', '小米');
INSERT INTO `car_master` VALUES (1034, '大H', 10017, '大黄蜂', '小米');
INSERT INTO `car_master` VALUES (1035, '小H', 10018, '雷诺', '小米');
INSERT INTO `car_master` VALUES (1036, '小G', 10019, '地狱天启', '小宋');
INSERT INTO `car_master` VALUES (1040, '小方', 1234, '奔驰', 'SONG');
INSERT INTO `car_master` VALUES (1041, '小黄', 123456, '法拉利', 'SONG');
INSERT INTO `car_master` VALUES (1042, '小', 123, '地方撒', 'SONG');

-- ----------------------------
-- Table structure for fix
-- ----------------------------
DROP TABLE IF EXISTS `fix`;
CREATE TABLE `fix`  (
  `fix_num` int NOT NULL AUTO_INCREMENT,
  `car_master_name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `fix_money` int NULL DEFAULT NULL,
  `fix_user` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `fix_part` varchar(225) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`fix_num`) USING BTREE,
  INDEX `Administration_name`(`car_master_name`) USING BTREE,
  INDEX `fix_user`(`fix_user`) USING BTREE,
  INDEX `fix_part`(`fix_part`) USING BTREE,
  CONSTRAINT `fix_ibfk_1` FOREIGN KEY (`car_master_name`) REFERENCES `car_master` (`car_master_name`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `fix_ibfk_2` FOREIGN KEY (`fix_user`) REFERENCES `administration` (`Administration_name`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `fix_ibfk_3` FOREIGN KEY (`fix_part`) REFERENCES `part` (`part_name`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1027 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of fix
-- ----------------------------
INSERT INTO `fix` VALUES (1022, '小A', 3000, 'SONG', '奔驰小灯');
INSERT INTO `fix` VALUES (1023, '小B', 4000, 'QI', '奔驰后视镜');
INSERT INTO `fix` VALUES (1024, '小D', 5000, 'BIN', '特斯拉小灯');
INSERT INTO `fix` VALUES (1025, '小E', 6000, '小张', '奔驰前车灯');
INSERT INTO `fix` VALUES (1026, '小B', 4000, '小张', '特斯拉尾灯');

-- ----------------------------
-- Table structure for part
-- ----------------------------
DROP TABLE IF EXISTS `part`;
CREATE TABLE `part`  (
  `part_num` int NOT NULL AUTO_INCREMENT,
  `part_name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `part_money` int NULL DEFAULT NULL,
  `part_left_num` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `part_start` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`part_num`) USING BTREE,
  INDEX `Administration_name`(`part_name`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 10010 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of part
-- ----------------------------
INSERT INTO `part` VALUES (10001, '奔驰小灯', 1000, '20', '广东');
INSERT INTO `part` VALUES (10002, '奔驰后视镜', 2000, '63', '广东');
INSERT INTO `part` VALUES (10003, '奔驰尾灯', 3000, '56', '广东');
INSERT INTO `part` VALUES (10004, '奔驰前车灯', 3000, '56', '广东');
INSERT INTO `part` VALUES (10005, '特斯拉小灯', 1000, '45', '浙江');
INSERT INTO `part` VALUES (10006, '特斯拉尾灯', 2000, '63', '浙江');
INSERT INTO `part` VALUES (10007, '法拉利小灯', 3000, '10', '北京');
INSERT INTO `part` VALUES (10008, '法拉利尾灯', 6000, '5', '北京');

SET FOREIGN_KEY_CHECKS = 1;
