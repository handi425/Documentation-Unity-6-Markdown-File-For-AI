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

#  [Camera](Camera.html).projectionMatrix

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

public [Matrix4x4](Matrix4x4.html) projectionMatrix;

### Description

Set a custom projection matrix.

If you change this matrix, the camera no longer updates its rendering based on
its [fieldOfView](Camera-fieldOfView.html). Moreover, this leaves the camera's
[nearClipPlane](Camera-nearClipPlane.html) and [farClipPlane](Camera-
farClipPlane.html) unchanged, so you need to update those manually to avoid
inconsistencies. This lasts until you call
[ResetProjectionMatrix](Camera.ResetProjectionMatrix.html).  
  
Use a custom projection only if you really need a non-standard projection.
This property is used by Unity's water rendering to setup an _oblique
projection_ matrix. Using custom projections requires good knowledge of
transformation and projection matrices.  
  
Note that projection matrix passed to shaders can be modified depending on
platform and other state. If you need to calculate projection matrix for
shader use from camera's projection, use
[GL.GetGPUProjectionMatrix](GL.GetGPUProjectionMatrix.html).  
  
Additional resources: [Camera.nonJitteredProjectionMatrix](Camera-
nonJitteredProjectionMatrix.html)

    
    
    // Make camera wobble in a funky way!
    using UnityEngine;
    using System.Collections;  
      
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        public [Matrix4x4](Matrix4x4.html) originalProjection;
        [Camera](Camera.html) cam;  
      
        void Start()
        {
            cam = GetComponent<[Camera](Camera.html)>();
            originalProjection = cam.projectionMatrix;
        }  
      
        void [Update](PlayerLoop.Update.html)()
        {
            [Matrix4x4](Matrix4x4.html) p = originalProjection;
            p.m01 += [Mathf.Sin](Mathf.Sin.html)([Time.time](Time-time.html) * 1.2F) * 0.1F;
            p.m10 += [Mathf.Sin](Mathf.Sin.html)([Time.time](Time-time.html) * 1.5F) * 0.1F;
            cam.projectionMatrix = p;
        }
    }
    
    
    
    // Set an off-center projection, where perspective's vanishing
    // point is not necessarily in the center of the screen.
    //
    // left/right/top/bottom define near plane size, i.e.
    // how offset are corners of camera's near plane.
    // Tweak the values and you can see camera's frustum change.  
      
    using UnityEngine;
    using System.Collections;  
      
    [[ExecuteInEditMode](ExecuteInEditMode.html)]
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        public float left = -0.2F;
        public float right = 0.2F;
        public float top = 0.2F;
        public float bottom = -0.2F;
        void LateUpdate()
        {
            [Camera](Camera.html) cam = [Camera.main](Camera-main.html);
            [Matrix4x4](Matrix4x4.html) m = PerspectiveOffCenter(left, right, bottom, top, cam.nearClipPlane, cam.farClipPlane);
            cam.projectionMatrix = m;
        }  
      
        static [Matrix4x4](Matrix4x4.html) PerspectiveOffCenter(float left, float right, float bottom, float top, float near, float far)
        {
            float x = 2.0F * near / (right - left);
            float y = 2.0F * near / (top - bottom);
            float a = (right + left) / (right - left);
            float b = (top + bottom) / (top - bottom);
            float c = -(far + near) / (far - near);
            float d = -(2.0F * far * near) / (far - near);
            float e = -1.0F;
            [Matrix4x4](Matrix4x4.html) m = new [Matrix4x4](Matrix4x4.html)();
            m[0, 0] = x;
            m[0, 1] = 0;
            m[0, 2] = a;
            m[0, 3] = 0;
            m[1, 0] = 0;
            m[1, 1] = y;
            m[1, 2] = b;
            m[1, 3] = 0;
            m[2, 0] = 0;
            m[2, 1] = 0;
            m[2, 2] = c;
            m[2, 3] = d;
            m[3, 0] = 0;
            m[3, 1] = 0;
            m[3, 2] = e;
            m[3, 3] = 0;
            return m;
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

