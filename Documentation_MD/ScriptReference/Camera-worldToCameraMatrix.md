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

#  [Camera](Camera.html).worldToCameraMatrix

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

public [Matrix4x4](Matrix4x4.html) worldToCameraMatrix;

### Description

Matrix that transforms from world to camera space.

This matrix is often referred to as "view matrix" in graphics literature.  
  
Use this to calculate the Camera space position of GameObjects or to provide a
custom Camera's location that is not based on the transform.  
  
Note that camera space matches OpenGL convention: camera's forward is the
negative Z axis. This is different from Unity's convention, where forward is
the positive Z axis.  
  
If you change this matrix, the camera no longer updates its rendering based on
its [Transform](Transform.html). This lasts until you call
[ResetWorldToCameraMatrix](Camera.ResetWorldToCameraMatrix.html).

    
    
    // Offsets camera's rendering from the transform's position.
    using UnityEngine;
    using System.Collections;  
      
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        public [Vector3](Vector3.html) offset = new [Vector3](Vector3.html)(0, 1, 0);
        [Camera](Camera.html) cam;  
      
        void Start()
        {
            cam = GetComponent<[Camera](Camera.html)>();
        }  
      
        void LateUpdate()
        {
            [Vector3](Vector3.html) camoffset = new [Vector3](Vector3.html)(-offset.x, -offset.y, offset.z);
            [Matrix4x4](Matrix4x4.html) m = [Matrix4x4.TRS](Matrix4x4.TRS.html)(camoffset, [Quaternion.identity](Quaternion-identity.html), new [Vector3](Vector3.html)(1, 1, -1));
            cam.worldToCameraMatrix = m * transform.worldToLocalMatrix;
        }
    }
    

Additional resources: [Matrix4x4.LookAt](Matrix4x4.LookAt.html),
[CommandBuffer.SetViewMatrix](Rendering.CommandBuffer.SetViewMatrix.html).

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

