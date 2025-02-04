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

#  [Plane](Plane.html).GetSide

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

public bool GetSide([Vector3](Vector3.html) point);

### Description

Is a point on the positive side of the plane?

    
    
    using UnityEngine;
    using System.Collections;  
      
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        public [Plane](Plane.html) goalLine1;
        public [Plane](Plane.html) goalLine2;
        public [Plane](Plane.html) leftSideLine;
        public [Plane](Plane.html) rightSideLine;  
      
        int GoalScored([Vector3](Vector3.html) ballPos)
        {
            // If the ball is within the sidelines...
            if (!leftSideLine.GetSide(ballPos) && !rightSideLine.GetSide(ballPos))
            {
                // If the ball is over goal line 1 then it's a goal for team 1...
                if (goalLine1.GetSide(ballPos))
                {
                    return 1;
                }
                // ...else if the ball is over goal line 2 then it's a goal for team 2.
                else if (goalLine2.GetSide(ballPos))
                {
                    return 2;
                }
            }  
      
            // Otherwise, it isn't a goal for either team.
            return 0;
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

