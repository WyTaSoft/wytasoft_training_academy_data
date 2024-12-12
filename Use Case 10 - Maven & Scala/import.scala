package com.wts.kayan.app.utility

import com.typesafe.config.Config
import org.apache.spark.sql.{Column, DataFrame, SparkSession}
import org.slf4j.LoggerFactory
import org.apache.hadoop.fs.{FileSystem, Path}
import org.apache.spark.SparkContext
import org.apache.spark.sql.functions.lit
import org.apache.spark.sql.types.StructType

import java.io.{BufferedReader, InputStreamReader, Reader}
import java.text.SimpleDateFormat
import java.util.Date