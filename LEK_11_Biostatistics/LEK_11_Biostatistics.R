# ####################################################################
# ### Exam  Statistics   2022                             ###
# ####################################################################
#  email: xxxxxxxxxxxxx@xxxxx.xxx


#  Please give your answers underneath the question,
#  referencing question numbers.
#  Please format text answers as comments.
pacman::p_load("DiscriMiner", "tidyverse", "wrappedtools", "readr")

# F1: Please generate the following sequences of numbers:
#   f1a: Integers between 75 and 50
         f1a <- seq(from=75, to=50, by=-1)
#   f1b: 500 random numbers from a uniform distribution
#        between 18 and 85
         set.seed(31052022)
         f1b <- runif(n = 500, max=85, min=18)
#   f1c: 500 random numbers from a Normal distribution 
#        with mean=100 and SD=10
         set.seed(31052022)
         f1c <- rnorm(n=500, mean=100, sd=10)
#   f1d: 100 random numbers from a Poisson distribution
#        with lambda=10
         set.seed(31052022)
         f1d <- rpois(n=100, lambda = 10)
#   f1e: 6 Lotto numbers between 1 and 49 ("6 aus 49").
         set.seed(31052022)
         f1e <- sample(x=49, size=6, replace=FALSE)

# F2: Test the numbers you generated in F1 against the 
#     Normal distribution, create a table structure
#     with the probabilities of a random deviation from 
#     Normality
         # Ho: numbers come from a normal distribution
         # Ha: numbers do not come from a normal distribution
         # For vectors with p-values less than or equal to 0.05 
         # we reject Ho (unexpected results are associated with 
         # a small sample size, e.g. f1e)
         
         my_tibble <- tibble(Numbers=c("f1a", "f1b","f1c","f1d","f1e"),
                             pvalue=NA_character_)

           my_tibble$pvalue[1] <- shapiro.test(f1a)$p.value %>% formatP()
           my_tibble$pvalue[2] <- shapiro.test(f1b)$p.value %>% formatP()
           my_tibble$pvalue[3] <- shapiro.test(f1c)$p.value %>% formatP()
           my_tibble$pvalue[4] <- shapiro.test(f1d)$p.value %>% formatP()
           my_tibble$pvalue[5] <- shapiro.test(f1e)$p.value %>% formatP()
           
           my_tibble %>% 
             flextable() %>% 
             set_table_properties(width=1, layout="autofit") 
           # Ho: sample come from a normal distribution
           # p-values which are greater than 0.05 indicate that sample can                  come from a normal distribution (f1a, f1c, f1e)
           
# F3: Please explain the following terms in your own words
#     (rather than just copy/pasting from wikipedia)
#     f3a: standard deviation
           # the average spread around the mean
#     f3b: standard error of the mean
           # standard deviation of a statistic (show how different the
           # true mean from the sample mean) 
#     f3c: significance
           # it is a Type I Error rate (alpha ) - false positives
#     f3d: statistical power
           # probability to conclude that the drag works when it does
#     f3e: sensitivity
           # probability that, if we you truly have the disease, the 
           # diagnostic test will catch it.
#     f3f: specificity
           # probability that, if we you truly do not have the disease, 
           # the test will register negative.
           
           

# F4: Please name the class / function for test statistics 
#     in the following cases:
#     f4a: Multiple comparison of mean values for 3 or
#         more groups for a gaussian measure
           # One-way ANOVA /anova()

#     f4b: Comparison of central tendencies for 
#          ordinal data between two groups
           # Wilcoxon Rank Sum (Mann-Whitney-U test)
           # wilcox.test()

#F5: Please analyze the dataset bordeaux 
#    from the package DiscriMiner.
           head(bordeaux)
#     F5a: Create a box plot for rain level, 
#          divided by quality, using ggplot.
           bordeaux %>% 
             ggplot(aes(x=quality, y=rain)) +
             geom_boxplot()+
             geom_beeswarm(alpha=0.5)
           
#     f5b: Test, if the differences you observe in f5a 
#          could be a chance outcome,
#          formulate the appropriate Null hypothesis.
           # Ho: mu1=mu2=mu3
           # quality is a factor
           # normality assumption per group is met
           my_test <- lm(rain~quality, data=rawdata)
           my_test2 <- aov(rain~quality, data=rawdata)
           summary(my_test)
           an <- anova(my_test)
           an$`Pr(>F)`
           # p-value is less than 0.05 (significant), 
           # hence we reject Ho, i.e. we conclude that there is
           # a difference in means between groups (one or more
           # groups are from a different population).

#     f5c: Create a report table with descriptive statistics 
#          for temperature and rain for the levels
#          of quality.
           cn(bordeaux)
           rawdata <- bordeaux
           quantvars <- FindVars(c('tem','ra')) 
           report_qv<-tibble(Variable=quantvars$names, 
                             nCases=NA_character_, 
                             'mean\u00B1sd'='&nbsp;',
                             `bad:mean±sd`=NA_character_,
                             `medium:mean±sd`=NA_character_,
                             `good:mean±sd`=NA_character_,
                              BadNormal=NA_character_,
                              MediumNormal=NA_character_,
                              GoodNormal=NA_character_)
           
           ndig<-3
          
           for (var_i in seq_len(quantvars$count)) {
             
             report_qv$nCases[var_i] <- length(na.omit(
               rawdata[[quantvars$index[var_i]]]))
             
             report_qv$`mean±sd`[var_i] <-
               meansd(rawdata %>% 
                      pull(quantvars$index[var_i]), 
                      roundDig = ndig)
             
             report_qv$`bad:mean±sd`[var_i] <-
               meansd(rawdata %>% 
                        dplyr::filter(quality=="bad") %>% 
                        pull(quantvars$index[var_i]), 
                      roundDig = ndig)
             
             report_qv$`medium:mean±sd`[var_i] <-
               meansd(rawdata %>% 
                        dplyr::filter(quality=="medium") %>% 
                        pull(quantvars$index[var_i]), 
                      roundDig = ndig)
             
             report_qv$`good:mean±sd`[var_i] <-
               meansd(rawdata %>% 
                        dplyr::filter(quality=="good") %>% 
                        pull(quantvars$index[var_i]), 
                      roundDig = ndig)
             
             report_qv$BadNormal[var_i] <-
               shapiro.test(rawdata %>%
                dplyr::filter(quality=="bad") %>%
              pull(quantvars$index[var_i]))$p.value %>% 
               formatP() 
             
             report_qv$MediumNormal[var_i] <-
               shapiro.test(rawdata %>%
                dplyr::filter(quality=="medium") %>%
                pull(quantvars$index[var_i]))$p.value %>% formatP() 
             
             report_qv$GoodNormal[var_i] <-
               shapiro.test(rawdata %>%
              dplyr::filter(quality=="good") %>%
              pull(quantvars$index[var_i]))$p.value %>% formatP() 
             
             }
           report_qv <- report_qv %>% 
             pivot_longer(cols = !Variable,
                          names_to="Statistics",
                          values_to = "Measure")
             
             
           # report_qv %>% 
           #   flextable() %>% 
           #   set_table_properties(width=1, layout="autofit") 
             
#     f5d: Export that table into a text file
#          with a ';' as separator
           write.table(report_qv, "Data/my_table.txt", 
                       append = FALSE, sep = ";",
                      col.names = TRUE)
           
#  F6: Create a matrix named 'participants' 
#       with 3 columns and 20 rows 
           my_matrix <- matrix(ncol = 3, nrow = 20)
#     F6a Put your first name in row 2 column 2 
#         and your family name in row 2 column 3
           my_matrix[2,2] <- "Vera"
           my_matrix[2,3] <- "Rykalina"
#     F6b: Fill column 1 with the words
#          "participant 1" to
#          "participant 20"
           my_matrix[,1] <-paste("participant", seq(1:20), sep=" ") 
#
# F7: Program a loop with an index from 1 to 10, 
#     that prints the text 'run' and index
  for (i_var in seq_len(10)) {
    
    print(paste("run", i_var, sep=" "))
    
  } 
# ######################################################
# ### Good luck!                                     ###
# ######################################################
