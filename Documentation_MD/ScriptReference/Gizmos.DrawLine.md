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

#  [Gizmos](Gizmos.html).DrawLine

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

public static void DrawLine([Vector3](Vector3.html) from,
[Vector3](Vector3.html) to);

### Description

Draws a line starting at `from` towards `to`.

If you need to draw many lines consider the
[Gizmos.DrawLineList](Gizmos.DrawLineList.html) or
[Gizmos.DrawLineStrip](Gizmos.DrawLineStrip.html) functions which are much
faster than repeatedly calling this function to draw lines individually.

    
    
    using UnityEngine;
    using System.Collections;  
      
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        public [Transform](Transform.html) target;  
      
        void OnDrawGizmosSelected()
        {
            if (target != null)
            {
                // Draws a blue line from this transform to the target
                [Gizmos.color](Gizmos-color.html) = [Color.blue](Color-blue.html);
                [Gizmos.DrawLine](Gizmos.DrawLine.html)(transform.position, target.position);
            }
        }
    }
    

Additional resources: [Gizmos.DrawLineList](Gizmos.DrawLineList.html),
[Gizmos.DrawLineStrip](Gizmos.DrawLineStrip.html).

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

