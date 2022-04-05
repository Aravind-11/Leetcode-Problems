# Maximum sum leaf to root path
## Medium 
<div class="problem-statement">
                <p><a onclick="gtagHelperFunction('clickopen','salesevent_gsc_problemspage_promobanner')" href="https://practice.geeksforgeeks.org/summer-carnival-2022?utm_source=practiceproblems&amp;utm_medium=problemspromobanner&amp;utm_campaign=gsc22" target="_blank"></a></p><div style="margin: 14px 0px !important;" class="row"><a onclick="gtagHelperFunction('clickopen','salesevent_gsc_problemspage_promobanner')" href="https://practice.geeksforgeeks.org/summer-carnival-2022?utm_source=practiceproblems&amp;utm_medium=problemspromobanner&amp;utm_campaign=gsc22" target="_blank">             <div class="col-md-12" style="cursor:pointer;background: #EFF8F3 0% 0% no-repeat padding-box; display: flex; align-items: center; position:                 relative; padding: 1.5%; border-radius: 10px; display: inline-block; text-align: center; font-weight: 600; color: #333"> <img src="https://media.geeksforgeeks.org/img-practice/gcs2022thumbnail-1649059370.png" alt="Lamp" width="46" height="40" style="background: transparent 0% 0% no-repeat padding-box;opacity: 1; margin: 0 16px;" class="img-responsive"> Geeks Summer Carnival is LIVE NOW &nbsp; <i class="fa fa-external-link" aria-hidden="true"></i> </div></a></div><p><span style="font-size:18px">Given a Binary Tree, find the maximum sum path from a leaf to root.</span></p>

<p><br>
<strong><span style="font-size:18px">Example 1:</span></strong></p>

<pre><strong><span style="font-size:18px">Input:</span></strong>
<span style="font-size:18px">        1
       / \
      2   3 </span>
<span style="font-size:18px"><strong>Output:</strong>
4</span>
<strong><span style="font-size:18px">Explanation: </span></strong>
<span style="font-size:18px">Following the path 3 -&gt; 1, results in a
sum of 4, which is the maximum path sum
from leaf to root for the given tree.</span>
</pre>

<p><strong><span style="font-size:18px">Example 2:</span></strong></p>

<pre><strong><span style="font-size:18px">Input:</span></strong>
<span style="font-size:18px">       10
      /  \
    -2    7
    / \   
   8  -4    </span>
<span style="font-size:18px"><strong>Output:</strong>
17</span>
<strong><span style="font-size:18px">Explanation : </span></strong>
<span style="font-size:18px">Following the path 7 -&gt; 10, results in a
sum of 17, which is the maximum path sum
from leaf to root for the given tree.</span></pre>

<div><br>
<strong><span style="font-size:18px">Your task :</span></strong></div>

<div><span style="font-size:18px">You don't need to read input or print anything. Your task is to complete the function <strong>maxPathSum()</strong> which takes the root node of the tree as input and returns an integer denoting the maximum possible leaf to root path sum.</span></div>

<div><br>
<span style="font-size:18px"><strong>Expected Time Complexity:</strong> O(n) , where n = number of nodes</span></div>

<div><span style="font-size:18px"><strong>Expected Auxiliary Space:</strong> O(1)</span></div>

<div><br>
<strong><span style="font-size:18px">Constraints :&nbsp;</span></strong></div>

<div><span style="font-size:18px">1 &lt;= Number of nodes &lt;= 10^5</span></div>
 <p></p>
            </div>