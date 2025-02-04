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

#  [LineRenderer](LineRenderer.html).shadowBias

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

public float shadowBias;

### Description

Apply a shadow bias to prevent self-shadowing artifacts. The specified value
is the proportion of the line width at each segment.

    
    
    using UnityEngine;
    using System.Collections;  
      
    [[RequireComponent](RequireComponent.html)(typeof([LineRenderer](LineRenderer.html)))]
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        private [LineRenderer](LineRenderer.html) lr;  
      
        void Start()
        {
            lr = GetComponent<[LineRenderer](LineRenderer.html)>();
            lr.material = new [Material](Material.html)([Shader.Find](Shader.Find.html)("Standard"));
            lr.castShadows = true;
            lr.receiveShadows = true;
            lr.shadowBias = 0.3f;  
      
            // Set some positions
            [Vector3](Vector3.html)[] positions = new [Vector3](Vector3.html)[3];
            positions[0] = new [Vector3](Vector3.html)(-2.0f, -2.0f, 0.0f);
            positions[1] = new [Vector3](Vector3.html)(0.0f, 2.0f, 0.0f);
            positions[2] = new [Vector3](Vector3.html)(2.0f, -2.0f, 0.0f);
            lr.positionCount = positions.Length;
            lr.SetPositions(positions);
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

