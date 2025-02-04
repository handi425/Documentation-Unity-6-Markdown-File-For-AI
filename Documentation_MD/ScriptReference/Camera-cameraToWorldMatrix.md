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

#  [Camera](Camera.html).cameraToWorldMatrix

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

[Switch to Manual](../Manual/class-Camera.html "Go to Camera Component in the
Manual")

public [Matrix4x4](Matrix4x4.html) cameraToWorldMatrix;

### Description

Matrix that transforms from camera space to world space (Read Only).

Use this to calculate where in the world a specific camera space point is.  
  
Note that camera space matches OpenGL convention: camera's forward is the
negative Z axis. This is different from Unity's convention, where forward is
the positive Z axis.

    
    
    // Draw a yellow sphere in [Scene](SceneManagement.Scene.html) view at distance/
    // units along camera's viewing direction.  
      
    using UnityEngine;
    using System.Collections;  
      
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        public float distance = -1.0F;
        void OnDrawGizmosSelected()
        {
            [Matrix4x4](Matrix4x4.html) m = Camera.main.cameraToWorldMatrix;
            [Vector3](Vector3.html) p = m.MultiplyPoint(new [Vector3](Vector3.html)(0, 0, distance));
            [Gizmos.color](Gizmos-color.html) = [Color.yellow](Color-yellow.html);
            [Gizmos.DrawSphere](Gizmos.DrawSphere.html)(p, 0.2F);
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

