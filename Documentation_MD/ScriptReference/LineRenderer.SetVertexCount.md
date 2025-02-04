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

**Method group is Obsolete**  

#  [LineRenderer](LineRenderer.html).SetVertexCount

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

[Switch to Manual](../Manual/class-LineRenderer.html "Go to LineRenderer
Component in the Manual")

**Obsolete** Use positionCount instead.

## Declaration

public void SetVertexCount(int count);

### Description

Set the number of line segments.

Additional resources: [SetPosition](LineRenderer.SetPosition.html) function.  
  
Additional resources: [SetPositions](LineRenderer.SetPositions.html) function.

    
    
    using UnityEngine;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        // Creates a line renderer that follows a Sin() function
        // and animates it.  
      
        [Color](Color.html) c1 = [Color.yellow](Color-yellow.html);
        [Color](Color.html) c2 = [Color.red](Color-red.html);
        int lengthOfLineRenderer = 20;  
      
        void Start()
        {
            [LineRenderer](LineRenderer.html) lineRenderer = gameObject.AddComponent<[LineRenderer](LineRenderer.html)>();
            lineRenderer.material = new [Material](Material.html)([Shader.Find](Shader.Find.html)("Sprites/Default"));
            lineRenderer.SetColors(c1, c2);
            lineRenderer.SetWidth(0.2f, 0.2f);
            lineRenderer.SetVertexCount(lengthOfLineRenderer);
        }  
      
        void [Update](PlayerLoop.Update.html)()
        {
            [LineRenderer](LineRenderer.html) lineRenderer = GetComponent<[LineRenderer](LineRenderer.html)>();
            var points = new [Vector3](Vector3.html)[lengthOfLineRenderer];
            var t = [Time.time](Time-time.html);
            for (int i = 0; i < lengthOfLineRenderer; i++)
            {
                points[i] = new [Vector3](Vector3.html)(i * 0.5f, [Mathf.Sin](Mathf.Sin.html)(i + t), 0);
            }
            lineRenderer.SetPositions(points);
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

