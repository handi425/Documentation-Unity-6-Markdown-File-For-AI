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

#  [Coverage](TestTools.Coverage.html).GetSequencePointsFor

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

public static CoveredSequencePoint[] GetSequencePointsFor(MethodBase method);

### Parameters

method | The method to get the sequence points for.  
---|---  
  
### Returns

**CoveredSequencePoint[]** Array of sequence points.

### Description

Returns the coverage sequence points for the method you specify. See
[CoveredSequencePoint](TestTools.CoveredSequencePoint.html) for more
information about the coverage data this method returns.

    
    
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
            // And get the sequence points for the method.
            [CoveredSequencePoint](TestTools.CoveredSequencePoint.html)[] sequencePoints = [Coverage.GetSequencePointsFor](TestTools.Coverage.GetSequencePointsFor.html)(coveredMethodBase);  
      
            for (int i = 0; i < sequencePoints.Length; i++)
            {
                [Debug.Log](Debug.Log.html)("[File](Windows.File.html): " + sequencePoints[i].filename);
                [Debug.Log](Debug.Log.html)("Method Name: " + sequencePoints[i].method.ToString());
                [Debug.Log](Debug.Log.html)("Line: " + sequencePoints[i].line + " [Column](UIElements.Column.html): " + sequencePoints[i].column);
                [Debug.Log](Debug.Log.html)(" IL Offset: " + sequencePoints[i].ilOffset + " Hit Count: " + sequencePoints[i].hitCount);
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

