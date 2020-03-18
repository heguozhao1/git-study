{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "source": [
    "## 关于Python\n",
    "\n",
    "### Python简介\n",
    "\n",
    "Python是一种被广泛使用的高级编程语言，它的设计理念强调代码可读性，同时其语言也具有简洁性，允许程序员用更少的代码来表达概念。Python支持多种编程范式，包括面向对象的、命令式、函数式编程或面向过程的编程。它具有庞大而全面的标准库，可以轻易完成各种高级任务。"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "subslide"
    }
   },
   "source": [
    "### 下载与安装 \n",
    "\n",
    "目前Python有两个版本，一个是2.x版，一个是3.x版，且两个版本不兼容。由于3.x版越来越普及，所以本教程将以最新版本Python3.7为基础。\n",
    "\n",
    "在Linux上，通常默认安装Python；\n",
    "\n",
    "在Mac系统上，如果系统自带不是3.7版本，可从Python官网下载安装；（https://www.python.org/）\n",
    "\n",
    "在Windows系统上，建议安装Anaconda，它是一个开源的Python发行版本。（https://www.anaconda.com/）"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "subslide"
    }
   },
   "source": [
    "### 运行Python\n",
    "\n",
    "Python安装成功后，打开命令提示符窗口，输入python后，看到提示符变为“>>>”就表示我们已经在Python交互式环境中了，可以输入任何Python代码，回车后会立刻得到执行结果。\n",
    "\n",
    "输入exit()并回车，可以退出Python交互式环境（直接关掉命令行窗口也可以）。"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "source": [
    "## 基本运算"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "8"
      ]
     },
     "execution_count": 1,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "5 + 3"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "3"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "5 - 2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "3"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "2+1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "10"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "5 * 2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "25"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "5 ** 2  #幂"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "subslide"
    }
   },
   "source": [
    "注意：在Python中符号(^)的用法不再是求幂，而是“异或”,用于逻辑运算。"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "7"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "5 ^ 2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {
    "slideshow": {
     "slide_type": "subslide"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "2.5"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "5 / 2  #注意：两个整型数相除的结果是实型"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "2"
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "5 // 2  #地板除，即只取结果的整数部分"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "5 % 2  #取余"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "4"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "_ + 3  #在Python中，\"_\"可用于调用上次的结果"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "source": [
    "## 数据类型"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "source": [
    "### 字符串"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Li Feng'"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "a = \"Li Feng\"\n",
    "a"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "str"
      ]
     },
     "execution_count": 27,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "type(a)  #type()用于求数据类型"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "7"
      ]
     },
     "execution_count": 34,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(a)   #len()用于求字符串包含多少个字符"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {
    "slideshow": {
     "slide_type": "subslide"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'L'"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "a = \"Li Feng\"\n",
    "a[0]  #索引从0开始"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'n'"
      ]
     },
     "execution_count": 35,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "a[-2]  #负号表示倒数，即从右往左数"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Fe'"
      ]
     },
     "execution_count": 37,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "a[3:5]  #[3:5]处理为[3,5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Feng'"
      ]
     },
     "execution_count": 36,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "a[3:100]  #超出索引的部分忽略"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Feng'"
      ]
     },
     "execution_count": 33,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "a[3:]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "subslide"
    }
   },
   "source": [
    "字符串可以用加号连接，也可以与数字相乘，得到若干个一样的字符串"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Li   Feng'"
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "b = \"Li\"+\" \"*3+\"Feng\"\n",
    "b"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'666'"
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "'6' * 3"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {
    "slideshow": {
     "slide_type": "subslide"
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Li Feng\n"
     ]
    }
   ],
   "source": [
    "print(\"Li Feng\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hello \n",
      " World!\n"
     ]
    }
   ],
   "source": [
    "print(\"Hello \\n World!\")  #'\\n'为特殊字符，表示换行"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "metadata": {
    "scrolled": true,
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hello \\n World!\n"
     ]
    }
   ],
   "source": [
    "print(r\"Hello \\n World!\")  #加入r，不处理为特殊字符"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "source": [
    "### 列表"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 61,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [],
   "source": [
    "a = [1,2,3]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 62,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "list"
      ]
     },
     "execution_count": 62,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "type(a)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 63,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1"
      ]
     },
     "execution_count": 63,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "a[0]  #索引从0开始"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 64,
   "metadata": {
    "slideshow": {
     "slide_type": "subslide"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[1, 2, 3, 4]"
      ]
     },
     "execution_count": 64,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "a.append(4)  #往list中追加元素到末尾\n",
    "a"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 65,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[1, 2, 'a', 3, 4]"
      ]
     },
     "execution_count": 65,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "a.insert(2,'a')  #把元素插入到指定的位置\n",
    "a"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 66,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[1, 2, 3, 4]"
      ]
     },
     "execution_count": 66,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "a.remove('a')  #移除列表中第一个指定元素\n",
    "a"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 67,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[1, 2, 3, 4, 4, 5, 6]"
      ]
     },
     "execution_count": 67,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "b = [4,5,6]\n",
    "a.extend(b)  #将两个列表合并\n",
    "a"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 68,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[1, 2, 3, 4, 5, 6]"
      ]
     },
     "execution_count": 68,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "a.remove(4)  \n",
    "a"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 69,
   "metadata": {
    "slideshow": {
     "slide_type": "subslide"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[1, 2, 3, 4, 5]"
      ]
     },
     "execution_count": 69,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "del a[5]  #移除指定位置上的元素\n",
    "a"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 70,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "5"
      ]
     },
     "execution_count": 70,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "a.pop()  #移除list中的最后一个元素，并且返回该元素的值。"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 71,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[1, 2, 3, 4]"
      ]
     },
     "execution_count": 71,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "a"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 72,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "3"
      ]
     },
     "execution_count": 72,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "a.pop(2)  #移除指定位置元素，并返回该元素的值"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {
    "slideshow": {
     "slide_type": "subslide"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[1, 3, 2, 3]"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "a = [1,3,2,3]\n",
    "a"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[1, 2, 3, 3]"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "a.sort()  #按从小到大顺序排列\n",
    "a"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[3, 3, 2, 1]"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "a.reverse()  #将列表顺序颠倒\n",
    "a"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "2"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "a.count(3)  #计算列表中指定元素的个数"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "a.index(3)  #求列表中第一个指定元素的索引"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "subslide"
    }
   },
   "source": [
    "列表的值传递与址传递："
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "([3, 3, 2, 1], [3, 3, 2, 1], [3, 3, 2, 1])"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "c1 = a\n",
    "c2 = a[:]\n",
    "c3 = a.copy()\n",
    "c1,c2,c3"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[3, 3, 2, 1, 4]"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "a.append(4)\n",
    "a"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[[3, 3, 2, 1, 4], [3, 3, 2, 1], [3, 3, 2, 1]]"
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "[c1,c2,c3]  #c1与a同步变化，说明c1=a为地址传递，而c2，c3为值传递"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "subslide"
    }
   },
   "source": [
    "列表的嵌套使用："
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "list"
      ]
     },
     "execution_count": 45,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "matrix = [[1, 2, 3, 4],[5, 6, 7, 8, 9],[ 10, 11, 12]]\n",
    "type(matrix)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "metadata": {
    "scrolled": true,
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "7"
      ]
     },
     "execution_count": 46,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "matrix[1][2]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "subslide"
    }
   },
   "source": [
    "range经常无法使用某些方法，可以转成list进行操作："
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {
    "scrolled": true,
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[1, 3, 5]"
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "list(range(1,6,2))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "subslide"
    }
   },
   "source": [
    "列表生成式:把要生成的元素放到前面，后面跟for"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 76,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]"
      ]
     },
     "execution_count": 76,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "[x * x for x in range(1, 11)]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 77,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ']"
      ]
     },
     "execution_count": 77,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "[m + n for m in 'ABC' for n in 'XYZ']"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "source": [
    "### 集合"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{1, 2, 'a', 'bc'}"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "a = {1,2,2,'a','a','bc'}  #集合中元素不重复\n",
    "a"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "set"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "type(a)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 73,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 73,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "'a' in a  #用in判断是否在a中，返回true 或 false"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "False"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "'b' in a"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {
    "slideshow": {
     "slide_type": "subslide"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{1, 3, 'b', 'c'}"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "b = {1,3,'b','c'}\n",
    "b"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{1, 2, 3, 'a', 'b', 'bc', 'c'}"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "a | b #求集合的并"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{1}"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "a & b  #求集合的交"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{2, 'a', 'bc'}"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "a - b  #求集合的差，a-b表示在a中，不在b中的元素的集合"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{2, 3, 'a', 'b', 'bc', 'c'}"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "a ^ b   #求两集合的异或，a^b=(a | b)-(a & b)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {
    "slideshow": {
     "slide_type": "subslide"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'1', '2', '3', 'a', 'b'}"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "a = set('1223222abb')\n",
    "a"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "source": [
    "### 元组"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(1, 'a', 'b')"
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "a = 1,'a','b'   #元组由逗号分隔的多个值组成\n",
    "a"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 61,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "tuple"
      ]
     },
     "execution_count": 61,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "type(a)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {
    "slideshow": {
     "slide_type": "subslide"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "((1, 'a', 'b'), [1, 'c'])"
      ]
     },
     "execution_count": 23,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "b = [1,'c']\n",
    "c = a,b  #元组中可以嵌套不同类型的数据\n",
    "c"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(1, 'a', 'b')"
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "c[0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'c'"
      ]
     },
     "execution_count": 22,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "c[1][1]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "subslide"
    }
   },
   "source": [
    "元组是不可变的，但是它们可以包含可变对象。"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [
    {
     "ename": "TypeError",
     "evalue": "'tuple' object does not support item assignment",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-27-dd7deb8516d5>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m()\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[0mc\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;36m0\u001b[0m\u001b[1;33m]\u001b[0m \u001b[1;33m=\u001b[0m \u001b[1;36m1\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;31mTypeError\u001b[0m: 'tuple' object does not support item assignment"
     ]
    }
   ],
   "source": [
    "c[0] = 1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "((1, 'a', 'b'), [1, 2])"
      ]
     },
     "execution_count": 28,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "c[1][1]=2\n",
    "c"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "source": [
    "### 字典"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'Mike': 3759, 'Mary': 1462, 'Ning': 6839}\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "dict"
      ]
     },
     "execution_count": 35,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "tel = {'Mike':3759, 'Mary':1462, 'Ning':6839}\n",
    "print(tel)\n",
    "type(tel)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'Mike': 3759, 'Mary': 1462, 'Ning': 6839}"
      ]
     },
     "execution_count": 41,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "tel = dict(Mike = 3759, Mary = 1462, Ning = 6839)\n",
    "tel"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 60,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'Mike': 3759, 'Mary': 1462, 'Ning': 6839}"
      ]
     },
     "execution_count": 60,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "tel = dict([('Mike',3759),('Mary',1462),('Ning',6839)]) #将一个由关键字与值构成的元组对序列变成字典\n",
    "tel"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 67,
   "metadata": {
    "slideshow": {
     "slide_type": "subslide"
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "dict_keys(['Mike', 'Mary', 'Ning'])\n",
      "dict_values([3759, 1462, 6839])\n"
     ]
    }
   ],
   "source": [
    "print(tel.keys())\n",
    "print(tel.values())  #分别访问关键字与值"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 70,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['Mike', 'Mary', 'Ning']"
      ]
     },
     "execution_count": 70,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "list(tel.keys())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 68,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['Mary', 'Mike', 'Ning']"
      ]
     },
     "execution_count": 68,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "sorted(tel.keys())  #排序"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "3759"
      ]
     },
     "execution_count": 47,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "tel['Mike']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 48,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "'Mike' in tel"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "metadata": {
    "slideshow": {
     "slide_type": "subslide"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'Mike': 3759, 'Mary': 1462, 'Ning': 6839, 'Ada': 8080}"
      ]
     },
     "execution_count": 50,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "tel['Ada'] = 8080  #添加元素\n",
    "tel"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 56,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'Mike': 3759, 'Mary': 1462, 'Ning': 6839, 'Ada': 8090}"
      ]
     },
     "execution_count": 56,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "tel['Ada'] = 8090  #修改值\n",
    "tel"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 57,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'Mike': 3759, 'Ning': 6839, 'Ada': 8090}"
      ]
     },
     "execution_count": 57,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "del tel['Mary']  #删除指定元素\n",
    "tel"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "source": [
    "##  基本语句"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "subslide"
    }
   },
   "source": [
    "### 条件语句"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 71,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "True\n"
     ]
    }
   ],
   "source": [
    "if True:\n",
    "    print('True')  #基本语法"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 72,
   "metadata": {
    "scrolled": true,
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "3是奇数\n"
     ]
    }
   ],
   "source": [
    "n = 3  #判断奇偶性\n",
    "if n % 2 == 0:\n",
    "    print(n,'是偶数',sep = '')\n",
    "elif n % 2 == 1:\n",
    "    print(n,'是奇数',sep = '')\n",
    "else:\n",
    "    print(n,'既不是奇数也不是偶数',sep = '')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 74,
   "metadata": {
    "slideshow": {
     "slide_type": "subslide"
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "23  is not a perfect square\n"
     ]
    }
   ],
   "source": [
    "#判断一个100以内的数是否为完全平方数\n",
    "a=[x**2 for x in range(1,10)]\n",
    "n=23\n",
    "if n in a :\n",
    "    print(repr(n)+' is a perfect square') #n是一个int，不可以直接用加号连上字符串，可通过repr()函数将其变为字符串\n",
    "else:\n",
    "    print(n,' is not a perfect square')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "subslide"
    }
   },
   "source": [
    "### for循环"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 73,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0\n",
      "1\n",
      "2\n"
     ]
    }
   ],
   "source": [
    "for i in range(3):\n",
    "    print(i)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "subslide"
    }
   },
   "source": [
    "continue的用法："
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 74,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "3\n",
      "5\n",
      "7\n",
      "9\n"
     ]
    }
   ],
   "source": [
    "a = {3,2,5,7,9,10,8}\n",
    "for x in a:\n",
    "    if x % 2 == 0:\n",
    "        continue\n",
    "    print(x)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "source": [
    "break的用法："
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 75,
   "metadata": {
    "scrolled": true,
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0 1\n",
      "1 2\n",
      "2 4\n",
      "3 8\n"
     ]
    }
   ],
   "source": [
    "for i in range(5):                  \n",
    "    if 2 ** i < 10:\n",
    "        print(i,2 ** i)\n",
    "    else:\n",
    "        break"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "subslide"
    }
   },
   "source": [
    "求和：1+2+...+100"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 76,
   "metadata": {
    "scrolled": false,
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "5050\n"
     ]
    }
   ],
   "source": [
    "a=range(1,101)  \n",
    "sum=0\n",
    "for s in a:\n",
    "    sum=sum+s\n",
    "print(sum)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "subslide"
    }
   },
   "source": [
    "求: 5！"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 77,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "120\n"
     ]
    }
   ],
   "source": [
    "a=range(1,6)\n",
    "factorial=1\n",
    "for s in a :\n",
    "    factorial=factorial*s\n",
    "print(factorial)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "subslide"
    }
   },
   "source": [
    "求某数所有的因子："
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 78,
   "metadata": {
    "scrolled": true,
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Select a number :15\n",
      "[1, 3, 5, 15]\n"
     ]
    }
   ],
   "source": [
    "a=input('Select a number :')\n",
    "divisors=[]\n",
    "m=[value for value in range (1,int(a)+1)]\n",
    "for s in m:\n",
    "    if int(a)%s==0:\n",
    "        divisors.append(s)\n",
    "print(divisors)#find the set of divisors of a specific a given by users"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 78,
   "metadata": {
    "slideshow": {
     "slide_type": "subslide"
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Select a number :15\n",
      "15  is not a prime\n"
     ]
    }
   ],
   "source": [
    "##进一步的我们可以判断一个数是否为素数\n",
    "a=input('Select a number :')\n",
    "divisors=[]\n",
    "m=[value for value in range (1,int(int(a)**(1/2))+1)]\n",
    "for s in m:\n",
    "    if int(a)%s==0:\n",
    "        divisors.append(s)\n",
    "divisors.remove(1)\n",
    "flag='true'\n",
    "for divisor in divisors:\n",
    "    if int(a)%divisor==0:\n",
    "        flag='false'\n",
    "        break\n",
    "if flag=='true':\n",
    "    print(a,' is a prime')\n",
    "else:\n",
    "    print(a,' is not a prime')\n",
    "    \n",
    "    "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "subslide"
    }
   },
   "source": [
    "### while循环"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 79,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0 1\n",
      "1 2\n",
      "2 4\n",
      "3 8\n"
     ]
    }
   ],
   "source": [
    "a = 0\n",
    "while 2 ** a < 10:\n",
    "    print(a,2 ** a)\n",
    "    a = a + 1"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "subslide"
    }
   },
   "source": [
    "求斐波那契数列的前n项："
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {
    "scrolled": true,
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "请输入项数(≥3)：15\n",
      "[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]\n"
     ]
    }
   ],
   "source": [
    "a=[1,1]\n",
    "k=3\n",
    "x=input('请输入项数(≥3)：')\n",
    "while k<=int(x):\n",
    "    b=a[-1]+a[-2]\n",
    "    a.append(b)\n",
    "    k=k+1\n",
    "print(a)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "subslide"
    }
   },
   "source": [
    "求一个完全平方数的平方根:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Select an integer:24\n",
      "Its not a perfect square \n"
     ]
    }
   ],
   "source": [
    "xx=input('Select an integer:')\n",
    "x=int(xx)                    #注意xx是一个str，要进行运算必须转成int\n",
    "ans=0\n",
    "if  x>0:\n",
    "    while ans*ans<x:\n",
    "        ans=ans+1\n",
    "    if ans**2==x:\n",
    "        print('Its square root is '+ repr(ans))\n",
    "    else:\n",
    "        print('Its not a perfect square ')#来自用户的输入可能并不是完全平方数，要考虑并返回一个相应的提示\n",
    "else:\n",
    "    print('It is not a positive integer')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "subslide"
    }
   },
   "source": [
    "用while 配合 k的计数器，进行数的分组操作"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 79,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[48, 45, 42, 39, 36, 33, 30, 27, 24, 21, 18, 15, 12, 9, 6, 3, '3k']\n",
      "[49, 46, 43, 40, 37, 34, 31, 28, 25, 22, 19, 16, 13, 10, 7, 4, 1, '3k+1']\n",
      "[47, 44, 41, 38, 35, 32, 29, 26, 23, 20, 17, 14, 11, 8, 5, 2, '3k+2']\n"
     ]
    }
   ],
   "source": [
    "x=[value for value in range(1,50)]\n",
    "a=['3k']\n",
    "b=['3k+1']\n",
    "c=['3k+2']\n",
    "t=len(x)\n",
    "k=1\n",
    "while k<=t: #此处需要变量，t不能换为len(x)\n",
    "    if x[0]%3==0:\n",
    "         a.insert(0,x[0])\n",
    "         x.remove(x[0])\n",
    "    elif  x[0]%3==1:\n",
    "         b.insert(0,x[0])\n",
    "         x.remove(x[0])\n",
    "    else:\n",
    "         c.insert(0,x[0])\n",
    "         x.remove(x[0])\n",
    "    k=k+1\n",
    "\n",
    "else:\n",
    "    print(a)\n",
    "    print(b)\n",
    "    print(c)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "source": [
    "## 导入模块及函数 "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "subslide"
    }
   },
   "source": [
    "math模块提供了许多对浮点数的数学运算函数，dir(math) 命令可以查看 math 查看包中的内容"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 82,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1.0"
      ]
     },
     "execution_count": 82,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import math\n",
    "math.exp(0)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 83,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1.0"
      ]
     },
     "execution_count": 83,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import math as mt\n",
    "mt.exp(0)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 84,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1.0"
      ]
     },
     "execution_count": 84,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from math import exp \n",
    "exp(0) "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 85,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1.0"
      ]
     },
     "execution_count": 85,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from math import exp as myexp \n",
    "myexp(0)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "subslide"
    }
   },
   "source": [
    "numpy（Numerical Python）提供了python对多维数组对象的支持"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 86,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[1, 2],\n",
       "       [3, 4]])"
      ]
     },
     "execution_count": 86,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import numpy as np\n",
    "A = np.array([[1,2],[3,4]])\n",
    "A"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 87,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[1, 3],\n",
       "       [2, 4]])"
      ]
     },
     "execution_count": 87,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "A.T  #求矩阵转置"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "subslide"
    }
   },
   "source": [
    "Scipy（Scientific Python）:可以利用numpy做更高级的数学，信号处理，优化，统计等"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 88,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[-2. ,  1. ],\n",
       "       [ 1.5, -0.5]])"
      ]
     },
     "execution_count": 88,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from scipy import linalg\n",
    "B = linalg.inv(A) # 求矩阵的逆\n",
    "B"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 89,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[1.0000000e+00, 0.0000000e+00],\n",
       "       [8.8817842e-16, 1.0000000e+00]])"
      ]
     },
     "execution_count": 89,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "A.dot(B)   #矩阵乘法"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "subslide"
    }
   },
   "source": [
    "matplotlib：一个 Python 的 2D绘图库"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 126,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[<matplotlib.lines.Line2D at 0xbb31240>]"
      ]
     },
     "execution_count": 126,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "import matplotlib.pyplot as plt\n",
    "\n",
    "x = [1,2,3,4,5,6]\n",
    "y = [3,4,6,2,4,8]\n",
    "\n",
    "plt.plot(x, y)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "source": [
    "## 函数 "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "subslide"
    }
   },
   "source": [
    "### 自定义函数 "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 91,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [],
   "source": [
    "def parity(n):\n",
    "    \"\"\"To judge whether an integer is odd or even.\"\"\"      # the function help\n",
    "    if n % 2 == 0:\n",
    "        print(n,'是偶数',sep = '')\n",
    "    elif n % 2 == 1:\n",
    "        print(n,'是奇数',sep = '')\n",
    "    else:\n",
    "        print(n,'既不是奇数也不是偶数',sep = '')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 92,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Help on function parity in module __main__:\n",
      "\n",
      "parity(n)\n",
      "    To judge whether an integer is odd or even.\n",
      "\n"
     ]
    }
   ],
   "source": [
    "help(parity)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 93,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "3是奇数\n"
     ]
    }
   ],
   "source": [
    "parity(3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 94,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "3.1既不是奇数也不是偶数\n"
     ]
    }
   ],
   "source": [
    "parity(3.1)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "subslide"
    }
   },
   "source": [
    "匿名函数：关键字lambda表示匿名函数，冒号前面的x表示函数参数，后面只能有一个表达式，不用写return，返回值就是该表达式的结果。"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 95,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "4"
      ]
     },
     "execution_count": 95,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "f = lambda x: x ** 2\n",
    "f(2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 84,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [],
   "source": [
    "def make_incrementor(n):\n",
    "    return lambda x: x + n  #返回一个函数"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 85,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [],
   "source": [
    "f = make_incrementor(42)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 86,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(42, 43)"
      ]
     },
     "execution_count": 86,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "f(0),f(1)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "subslide"
    }
   },
   "source": [
    "汉诺塔问题：定义一个函数，接收参数n，表示3个柱子A、B、C中第1个柱子A的盘子数量，然后打印出把所有盘子从A借助B移动到C的方法"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [],
   "source": [
    "def move(n, a, b, c):\n",
    "    if n == 1:\n",
    "            print(a, '-->', c)\n",
    "    else:\n",
    "        move(n-1, a, c, b)\n",
    "        move(1, a, b, c)\n",
    "        move(n-1, b, a, c)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "A --> C\n",
      "A --> B\n",
      "C --> B\n",
      "A --> C\n",
      "B --> A\n",
      "B --> C\n",
      "A --> C\n"
     ]
    }
   ],
   "source": [
    "move(3, 'A', 'B', 'C')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "subslide"
    }
   },
   "source": [
    "某些函数定义时设置了多个参数，使用默认参数可以简化该函数的调用："
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 92,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [],
   "source": [
    "def power(x, n=2):  #幂函数\n",
    "    s = 1\n",
    "    while n > 0:\n",
    "        s = s * x\n",
    "        n = n - 1\n",
    "    return s"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 90,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "25"
      ]
     },
     "execution_count": 90,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "power(5) #只输入一个数，默认求其平方"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 91,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "125"
      ]
     },
     "execution_count": 91,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "power(5,3)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "subslide"
    }
   },
   "source": [
    "functools.partial可以创建一个新的函数，这个新函数可以固定住原函数的部分参数，从而在调用时更简单"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 93,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "64"
      ]
     },
     "execution_count": 93,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import functools\n",
    "int2 = functools.partial(int, base=2)\n",
    "int2('1000000')     #相当于int('1000000',base = 2)，即默认二进制转换为十进制"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "subslide"
    }
   },
   "source": [
    "### 生成器(generator)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "source": [
    "如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator,可通过for循环来迭代它"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [],
   "source": [
    "def triangles(n):    #杨辉三角\n",
    "    L = [1]\n",
    "    for x in range(n):\n",
    "        yield L\n",
    "        L = [1] + [L[i] + L[i+1] for i in range(len(L)-1)] + [1]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1]\n",
      "[1, 1]\n",
      "[1, 2, 1]\n",
      "[1, 3, 3, 1]\n",
      "[1, 4, 6, 4, 1]\n",
      "[1, 5, 10, 10, 5, 1]\n",
      "[1, 6, 15, 20, 15, 6, 1]\n",
      "[1, 7, 21, 35, 35, 21, 7, 1]\n",
      "[1, 8, 28, 56, 70, 56, 28, 8, 1]\n",
      "[1, 9, 36, 84, 126, 126, 84, 36, 9, 1]\n"
     ]
    }
   ],
   "source": [
    "for x in triangles(10):     \n",
    "    print(x)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "subslide"
    }
   },
   "source": [
    "### 高阶函数"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "source": [
    "变量可以指向函数,函数名也是变量,一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数。"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [],
   "source": [
    "def add(x, y, f):\n",
    "    return f(x) + f(y)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "11"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "add(-5, 6, abs)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "subslide"
    }
   },
   "source": [
    "map(函数,可迭代序列)作为高阶函数，将传入的函数依次作用到序列的每个元素，并把结果作为新的迭代器返回。"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['1', '2', '3', '4', '5', '6', '7', '8', '9']"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9]))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [],
   "source": [
    "def normalize(name):  #将名字中的字母大小写规范化\n",
    "    name = name.lower()\n",
    "    name = name.capitalize()\n",
    "    return name"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['Adam', 'Lisa', 'Bart']"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "L = ['adam', 'LISA', 'barT']\n",
    "list(map(normalize, L))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "subslide"
    }
   },
   "source": [
    "reduce作为高阶函数，其效果是：reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)  (f必须接收两个参数)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [],
   "source": [
    "from functools import reduce\n",
    "def prod(L):  #求list中所有数的乘积\n",
    "    return reduce(lambda x, y: x * y, L )"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "945"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "prod([3, 5, 7, 9])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "subslide"
    }
   },
   "source": [
    "filter(函数，序列)：把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[1, 5, 9, 15]"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "list(filter(lambda x: x % 2 == 1, [1, 2, 4, 5, 6, 9, 10, 15]))  #返回list中的奇数"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "subslide"
    }
   },
   "source": [
    "sorted(序列，keys)：按照keys中函数作用后的结果进行排序，并按照对应关系返回list相应的元素"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[5, 9, -12, -21, 36]"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "sorted([36, 5, -12, 9, -21], key=abs)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[('Adam', 92), ('Bart', 66), ('Bob', 75), ('Lisa', 88)]\n",
      "[('Bart', 66), ('Bob', 75), ('Lisa', 88), ('Adam', 92)]\n",
      "[('Adam', 92), ('Lisa', 88), ('Bob', 75), ('Bart', 66)]\n"
     ]
    }
   ],
   "source": [
    "students = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]\n",
    "\n",
    "print(sorted(students, key=lambda x: x[0]))  #按名字\n",
    "print(sorted(students, key=lambda x: x[1]))  #按成绩从低到高\n",
    "print(sorted(students, key=lambda x: x[1], reverse=True))  #按成绩从高到低"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "source": [
    "## Python 的类"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "source": [
    "面向对象的程序设计思想，是把对象作为程序的基本单元：类是抽象的模板，实例是根据类创建出来的一个个具体的“对象”，每个对象都拥有相同的方法，但各自的数据可能不同。"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 104,
   "metadata": {
    "slideshow": {
     "slide_type": "subslide"
    }
   },
   "outputs": [],
   "source": [
    "class MyClass:\n",
    "    \"\"\"A simple example class\"\"\"\n",
    "    i = 12345\n",
    "    def f(self):\n",
    "        return 'hello world'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 95,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<__main__.MyClass at 0x4dedcf8>"
      ]
     },
     "execution_count": 95,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "MyClass()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 96,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "12345"
      ]
     },
     "execution_count": 96,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "MyClass.i  #引用属性"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 97,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<function __main__.MyClass.f(self)>"
      ]
     },
     "execution_count": 97,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "MyClass.f"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 98,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "3"
      ]
     },
     "execution_count": 98,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "MyClass.i = 3  #更改属性值\n",
    "MyClass.i"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 103,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1"
      ]
     },
     "execution_count": 103,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "MyClass.x = 1  #根据需要添加定义中没有的属性\n",
    "MyClass.x"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "subslide"
    }
   },
   "source": [
    "在创建实例的时候，定义一个特殊的__init__方法，把一些我们认为必须绑定的属性强制填写进去，可以起到模板的作用。"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [],
   "source": [
    "class Complex:\n",
    "    def __init__(self, realpart, imagpart):  #注意：特殊方法“__init__”前后分别有两个下划线\n",
    "        self.r = realpart\n",
    "        self.i = imagpart"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(3.0, -4.5)"
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "x = Complex(3.0, -4.5)\n",
    "x.r, x.i"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "source": [
    "##  读取文件 "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "subslide"
    }
   },
   "source": [
    "### 读取txt"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 100,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'C:\\\\Users\\\\Administrator\\\\Desktop'"
      ]
     },
     "execution_count": 100,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "pwd"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "source": [
    "在上述目录下创建一个test.txt,写入“Hello world！”"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [],
   "source": [
    "file_for_reading = open('test.txt', 'r')  #‘r’表示read"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Hello world! \\n'"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "file_for_reading.read()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [],
   "source": [
    "file_for_reading.close()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {
    "slideshow": {
     "slide_type": "subslide"
    }
   },
   "outputs": [],
   "source": [
    "file_for_writing = open('test.txt', 'w')  #‘w’表示write"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "18"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "file_for_writing.write('I love studying! \\n')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [],
   "source": [
    "file_for_writing.close()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "source": [
    "查看test.txt，发现内容变成了‘I love studying!’，说明原内容被覆盖"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {
    "slideshow": {
     "slide_type": "subslide"
    }
   },
   "outputs": [],
   "source": [
    "file_for_appending = open('test.txt','a') #‘a’表示append"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "14"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "file_for_appending.write('Hello world! \\n')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [],
   "source": [
    "file_for_appending.close()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "source": [
    "再次查看，发现原内容后加入了一行Hello world! "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "subslide"
    }
   },
   "source": [
    "由于close()很容易忘记，故推荐采用with语句，在语句执行完毕后自动关闭："
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [],
   "source": [
    "with open('test.txt','a') as file:\n",
    "    file.write('Nice to meet you! \\n')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "subslide"
    }
   },
   "source": [
    "### 读取csv"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "source": [
    "在工作目录下创建一个stocks.csv,由symbol,date,closing_price三列构成，并填充数据"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [],
   "source": [
    "import csv\n",
    "\n",
    "data = {'symbol':[], 'date':[], 'closing_price' : []}\n",
    "with open('stocks.csv', 'r') as f:\n",
    "    reader = csv.DictReader(f)\n",
    "    for row in reader:\n",
    "        data['symbol'].append(row[\"symbol\"])\n",
    "        data['date'].append(row[\"date\"])\n",
    "        data['closing_price'].append(float(row[\"closing_price\"]))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 112,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "dict_keys(['symbol', 'date', 'closing_price'])"
      ]
     },
     "execution_count": 112,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.keys()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 113,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[112.98, 112.4, 109.55, 108.72, 105.99]"
      ]
     },
     "execution_count": 113,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data['closing_price']"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "subslide"
    }
   },
   "source": [
    "也可使用pandas包中的read_csv()函数读取csv文件："
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "5\n",
      "<class 'pandas.core.frame.DataFrame'>\n"
     ]
    }
   ],
   "source": [
    "import pandas  \n",
    "data2 = pandas.read_csv('stocks.csv') \n",
    "print(len(data2)) \n",
    "print(type(data2))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>symbol</th>\n",
       "      <th>date</th>\n",
       "      <th>closing_price</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>AAPL</td>\n",
       "      <td>2015/1/23</td>\n",
       "      <td>112.98</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>AAPL</td>\n",
       "      <td>2015/1/22</td>\n",
       "      <td>112.40</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>AAPL</td>\n",
       "      <td>2015/1/21</td>\n",
       "      <td>109.55</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>AAPL</td>\n",
       "      <td>2015/1/20</td>\n",
       "      <td>108.72</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>AAPL</td>\n",
       "      <td>2015/1/16</td>\n",
       "      <td>105.99</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  symbol       date  closing_price\n",
       "0   AAPL  2015/1/23         112.98\n",
       "1   AAPL  2015/1/22         112.40\n",
       "2   AAPL  2015/1/21         109.55\n",
       "3   AAPL  2015/1/20         108.72\n",
       "4   AAPL  2015/1/16         105.99"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "symbol                AAPL\n",
       "date             2015/1/22\n",
       "closing_price        112.4\n",
       "Name: 1, dtype: object"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data2.iloc[1]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'2015/1/22'"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data2.iloc[1]['date']"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "source": [
    "## 文本处理 "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 116,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [],
   "source": [
    "import nltk"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 117,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[nltk_data] Downloading package punkt to\n",
      "[nltk_data]     C:\\Users\\Administrator\\AppData\\Roaming\\nltk_data...\n",
      "[nltk_data]   Package punkt is already up-to-date!\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 117,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "nltk.download('punkt')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "subslide"
    }
   },
   "source": [
    "分段为句："
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 118,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [],
   "source": [
    "para = \"Python is a widely used general-purpose, high-level programming language. Its design philosophy emphasizes code readability, and its syntax allows programmers to express concepts in fewer lines of code than would be possible in languages such as C++ or Java.\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 119,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['Python is a widely used general-purpose, high-level programming language.',\n",
       " 'Its design philosophy emphasizes code readability, and its syntax allows programmers to express concepts in fewer lines of code than would be possible in languages such as C++ or Java.']"
      ]
     },
     "execution_count": 119,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from nltk.tokenize import sent_tokenize \n",
    "sent_tokenize(para)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "subslide"
    }
   },
   "source": [
    "分段为词："
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 120,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['Python',\n",
       " 'is',\n",
       " 'a',\n",
       " 'widely',\n",
       " 'used',\n",
       " 'general-purpose',\n",
       " ',',\n",
       " 'high-level',\n",
       " 'programming',\n",
       " 'language',\n",
       " '.',\n",
       " 'Its',\n",
       " 'design',\n",
       " 'philosophy',\n",
       " 'emphasizes',\n",
       " 'code',\n",
       " 'readability',\n",
       " ',',\n",
       " 'and',\n",
       " 'its',\n",
       " 'syntax',\n",
       " 'allows',\n",
       " 'programmers',\n",
       " 'to',\n",
       " 'express',\n",
       " 'concepts',\n",
       " 'in',\n",
       " 'fewer',\n",
       " 'lines',\n",
       " 'of',\n",
       " 'code',\n",
       " 'than',\n",
       " 'would',\n",
       " 'be',\n",
       " 'possible',\n",
       " 'in',\n",
       " 'languages',\n",
       " 'such',\n",
       " 'as',\n",
       " 'C++',\n",
       " 'or',\n",
       " 'Java',\n",
       " '.']"
      ]
     },
     "execution_count": 120,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from nltk.tokenize import word_tokenize\n",
    "word_tokenize(para)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "subslide"
    }
   },
   "source": [
    "过滤掉语句中的“stopwords”："
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 122,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[nltk_data] Downloading package stopwords to\n",
      "[nltk_data]     C:\\Users\\Administrator\\AppData\\Roaming\\nltk_data...\n",
      "[nltk_data]   Package stopwords is already up-to-date!\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 122,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "nltk.download('stopwords')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'which', \"hadn't\", 'can', 'but', 'whom', 'won', 'too', 'under', 'more', 'to', 'that', 't', 'theirs', 'doing', 'your', 'those', 'up', 'doesn', 'again', 'hadn', 'mustn', 'an', 'in', 'didn', 'same', 'been', 'of', 'most', 'as', 'where', 'once', 'o', 'own', 'off', 'ain', 'hasn', 'no', 'during', 'all', 'weren', \"mustn't\", 'now', 'his', 'above', \"you've\", 'these', 'i', 'on', 'both', \"isn't\", 'between', 'the', 'her', 'don', 'itself', \"don't\", 'we', \"hasn't\", 'isn', 'wasn', 'here', 'than', 'then', \"weren't\", 'or', 'should', \"you'll\", 'my', 'be', 'being', 'so', 'y', 'until', \"wasn't\", 'd', 'only', 'had', 'aren', 'with', 'mightn', \"you'd\", 'its', 'haven', 'was', 'll', \"aren't\", \"shan't\", \"wouldn't\", 'wouldn', 'into', 'such', \"doesn't\", 'themselves', 'there', \"shouldn't\", 'some', 'she', \"couldn't\", 'do', 'for', 'while', 'any', 're', 'over', 'did', 'will', \"won't\", 'about', 'further', 'other', 'few', 'at', 'have', 'ma', 'they', 'me', 'is', 'out', 'having', 'why', \"you're\", 'yours', 'just', 'couldn', 'shan', 'he', 'very', 'our', 'shouldn', 'against', 'ours', 'herself', 'has', 'are', 'below', 'nor', 'm', 'a', 'needn', 'hers', 'what', 'after', 'from', 'because', 'not', 've', 'does', 'who', 'this', 'him', \"didn't\", 'and', 'were', 'when', \"that'll\", 'by', 'down', 'himself', 'their', 'how', 'yourselves', 'myself', \"she's\", 'before', 'them', \"it's\", 'through', 'am', 'you', \"mightn't\", 'yourself', 'each', 's', 'it', \"haven't\", \"should've\", 'ourselves', \"needn't\", 'if'}\n"
     ]
    }
   ],
   "source": [
    "from nltk.corpus import stopwords\n",
    "english_stops = set(stopwords.words('english'))\n",
    "print(english_stops)  #输出stopwords"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 121,
   "metadata": {
    "slideshow": {
     "slide_type": "subslide"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['Smoking', 'is', 'now', 'banned', 'in', 'many', 'places', 'of', 'work']"
      ]
     },
     "execution_count": 121,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from nltk.tokenize import RegexpTokenizer \n",
    "tokenizer = RegexpTokenizer(\"[\\w']+\") \n",
    "words = tokenizer.tokenize(\"Smoking is now banned in many places of work.\") \n",
    "words"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 124,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['Smoking', 'banned', 'many', 'places', 'work']"
      ]
     },
     "execution_count": 124,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "[word for word in words if word not in english_stops]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "subslide"
    }
   },
   "source": [
    "去掉词缀："
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 125,
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'cook'"
      ]
     },
     "execution_count": 125,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from nltk.stem import PorterStemmer\n",
    "stemmer = PorterStemmer()\n",
    "stemmer.stem('cooking')"
   ]
  }
 ],
 "metadata": {
  "celltoolbar": "Slideshow",
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.6"
  },
  "toc": {
   "base_numbering": 1,
   "nav_menu": {},
   "number_sections": true,
   "sideBar": true,
   "skip_h1_title": false,
   "title_cell": "Table of Contents",
   "title_sidebar": "Contents",
   "toc_cell": false,
   "toc_position": {},
   "toc_section_display": true,
   "toc_window_display": true
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
