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

#  [Coverage](TestTools.Coverage.html).ResetFor

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

public static void ResetFor(MethodBase method);

### Parameters

method | The method.  
---|---  
  
### Description

Resets the coverage data for the specified method.

    
    
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
      
            // Use reflection to get the MethodBase for CoverageClass.CoveredMethod2
            MethodBase coveredMethodBase = typeof(CoverageClass).GetMethod("CoveredMethod2");  
      
            // Reset the coverage for CoveredMethod2
            [Coverage.ResetFor](TestTools.Coverage.ResetFor.html)(coveredMethodBase);  
      
            // Now get the coverage stats for the CoveredMethod2.
            // Because coverage for CoveredMethod2 has been reset, the log
            // will show that the none of the method's sequence points
            // have been covered.
            [CoveredMethodStats](TestTools.CoveredMethodStats.html) stats = [Coverage.GetStatsFor](TestTools.Coverage.GetStatsFor.html)(coveredMethodBase);  
      
            [Debug.Log](Debug.Log.html)("Method Name: " + stats.method.ToString());
            [Debug.Log](Debug.Log.html)("Method has " + stats.totalSequencePoints + " sequence points");
            int coveredSequencePoints = stats.totalSequencePoints - stats.uncoveredSequencePoints;
            [Debug.Log](Debug.Log.html)("of which " + coveredSequencePoints + " were covered.");
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

