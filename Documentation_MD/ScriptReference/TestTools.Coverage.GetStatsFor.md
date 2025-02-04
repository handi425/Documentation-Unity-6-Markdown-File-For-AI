[ ]()

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

LanguageEnglish

  * [English]()

  * C#

[ ](https://docs.unity3d.com)

## Scripting API

Version: Unity 6 Select a different version

LanguageEnglish

  * [English]()

#  [Coverage](TestTools.Coverage.html).GetStatsFor

Leave feedback

Suggest a change

## Success!

Thank you for helping us improve the quality of Unity Documentation. Although
we cannot accept all submissions, we do read each suggested change from our
users and will make updates where applicable.

Close

## Submission failed

For some reason your suggested change could not be submitted. Please <a>try
again</a> in a few minutes. And thank you for taking the time to help us
improve the quality of Unity Documentation.

Close

Your name Your email Suggestion* Submit suggestion

Cancel

[ ]()

## Declaration

public static
[TestTools.CoveredMethodStats](TestTools.CoveredMethodStats.html)
GetStatsFor(MethodBase method);

### Parameters

method | The method to get coverage statistics for.  
---|---  
  
### Returns

**CoveredMethodStats** Coverage summary.

### Description

Returns the coverage summary for the specified method. See
[CoveredMethodStats](TestTools.CoveredMethodStats.html) for more information
about the coverage statistics returned by this method.

    
    
    using UnityEngine;
    using UnityEngine.TestTools;
    using System.Reflection;  
      
    public class CoverageClass
    {
        // A simple test method to get coverage information from.
        // If the method is called with incrementValue set to true,
        // the method will have complete coverage. If incrementValue
        // is false, the coverage will be incomplete.
        public int CoveredMethod(bool incrementValue)
        {
            int value = 0;
            if (incrementValue)
            {
                value++;
            }  
      
            return value;
        }
    }  
      
    public class CoverageExample : [MonoBehaviour](MonoBehaviour.html)
    {
        void Start()
        {
            // Create an instance of the test class and call the test method
            // to make sure the method has had some coverage. Note in this example,
            // we're passing false into the method to make sure the coverage
            // is incomplete.
            CoverageClass coverageClasss = new CoverageClass();
            int value = coverageClasss.CoveredMethod(false);  
      
            // Use reflection to get the MethodBase for CoverageClass.CoveredMethod
            MethodBase coveredMethodBase = typeof(CoverageClass).GetMethod("CoveredMethod");
            // And get the coverage stats for the method.
            [CoveredMethodStats](TestTools.CoveredMethodStats.html) stats = [Coverage.GetStatsFor](TestTools.Coverage.GetStatsFor.html)(coveredMethodBase);  
      
            [Debug.Log](Debug.Log.html)("CoveredMethod has " + stats.totalSequencePoints + " sequence points");
            int coveredSequencePoints = stats.totalSequencePoints - stats.uncoveredSequencePoints;
            [Debug.Log](Debug.Log.html)("of which " + coveredSequencePoints + " were covered.");
        }
    }
    

* * *

## Declaration

public static CoveredMethodStats[] GetStatsFor(MethodBase[] methods);

### Parameters

methods | The array of methods.  
---|---  
  
### Returns

**CoveredMethodStats[]** Array of coverage summaries.

### Description

Returns an array of coverage summaries for the specified array of methods.

    
    
    using UnityEngine;
    using UnityEngine.TestTools;
    using System.Reflection;
    using [System](Rendering.VirtualTexturing.System.html);  
      
    // A simple test class to get coverage information for.
    public class CoverageClass
    {
        public bool CoveredMethod1()
        {
            return true;
        }  
      
        public bool CoveredMethod2()
        {
            return false;
        }
    }  
      
    public class CoverageExample : [MonoBehaviour](MonoBehaviour.html)
    {
        void Start()
        {
            // Create an instance of the test class and call the test methods
            // to make sure the class has had some coverage.
            CoverageClass coverageClasss = new CoverageClass();
            coverageClasss.CoveredMethod1();
            coverageClasss.CoveredMethod2();  
      
            // Get the Type of the CoverageClass
            Type coverageClassType = typeof(CoverageClass);  
      
            // Use reflection to get an array of MethodBases for the two methods
            // in CoverageClass.
            MethodBase[] coveredMethodBaseArray =
            {
                coverageClassType.GetMethod("CoveredMethod1"),
                coverageClassType.GetMethod("CoveredMethod2")
            };  
      
            // And get the coverage stats for the methods.
            [CoveredMethodStats](TestTools.CoveredMethodStats.html)[] stats = [Coverage.GetStatsFor](TestTools.Coverage.GetStatsFor.html)(coveredMethodBaseArray);  
      
            for (int i = 0; i < stats.Length; i++)
            {
                [Debug.Log](Debug.Log.html)("Method Name: " + stats[i].method.ToString());
                [Debug.Log](Debug.Log.html)("Method has " + stats[i].totalSequencePoints + " sequence points");
                int coveredSequencePoints = stats[i].totalSequencePoints - stats[i].uncoveredSequencePoints;
                [Debug.Log](Debug.Log.html)("of which " + coveredSequencePoints + " were covered.");
            }
        }
    }
    

* * *

## Declaration

public static CoveredMethodStats[] GetStatsFor(Type type);

### Parameters

type | The type.  
---|---  
  
### Returns

**CoveredMethodStats[]** Array of coverage summaries.

### Description

Returns an array of coverage summaries for the specified type.

    
    
    using UnityEngine;
    using UnityEngine.TestTools;
    using [System](Rendering.VirtualTexturing.System.html);  
      
    // A simple test class to get coverage information for.
    public class CoverageClass
    {
        public bool CoveredMethod1()
        {
            return true;
        }  
      
        public bool CoveredMethod2()
        {
            return false;
        }
    }  
      
    public class CoverageExample : [MonoBehaviour](MonoBehaviour.html)
    {
        void Start()
        {
            // Create an instance of the test class and call the test methods
            // to make sure the class has had some coverage.
            CoverageClass coverageClasss = new CoverageClass();
            coverageClasss.CoveredMethod1();
            coverageClasss.CoveredMethod2();  
      
            // Get the Type of the CoverageClass
            Type coverageClassType = typeof(CoverageClass);
            // And get the coverage stats for all of the methods of the type.
            // Note that this will include class's default constructor.
            [CoveredMethodStats](TestTools.CoveredMethodStats.html)[] stats = [Coverage.GetStatsFor](TestTools.Coverage.GetStatsFor.html)(coverageClassType);  
      
            for (int i = 0; i < stats.Length; i++)
            {
                [Debug.Log](Debug.Log.html)("Method Name: " + stats[i].method.ToString());
                [Debug.Log](Debug.Log.html)("Method has " + stats[i].totalSequencePoints + " sequence points");
                int coveredSequencePoints = stats[i].totalSequencePoints - stats[i].uncoveredSequencePoints;
                [Debug.Log](Debug.Log.html)("of which " + coveredSequencePoints + " were covered.");
            }
        }
    }
    

Is something described here not working as you expect it to? It might be a
**Known Issue**. Please check with the Issue Tracker at
[issuetracker.unity3d.com](https://issuetracker.unity3d.com).

Copyright ©2005-2025 Unity Technologies. All rights reserved. Built from:
6000.0.36f1 (02b661dc617c). Built on: 2025-01-14.

[Tutorials](https://unity3d.com/learn) [Community
Answers](https://answers.unity3d.com) [Knowledge
Base](https://support.unity3d.com/hc/en-us)
[Forums](https://forum.unity3d.com) [Asset Store](https://unity3d.com/asset-
store) [Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)
[Legal](https://unity.com/legal) [Privacy
Policy](https://unity.com/legal/privacy-policy)
[Cookies](https://unity.com/legal/cookie-policy) [Do Not Sell or Share My
Personal Information](https://unity.com/legal/do-not-sell-my-personal-
information)

[Your Privacy Choices (Cookie Settings)](javascript:void\(0\);)

