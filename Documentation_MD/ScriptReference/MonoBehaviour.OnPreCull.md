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

#  [MonoBehaviour](MonoBehaviour.html).OnPreCull()

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

[Switch to Manual](../Manual/class-MonoBehaviour.html "Go to MonoBehaviour
Component in the Manual")

### Description

[Event function](../Manual/event-functions.html) that Unity calls before a
[Camera](Camera.html) culls the scene.

In the Built-in Render Pipeline, Unity calls `OnPreCull` on MonoBehaviours
that are attached to the same GameObject as an enabled [Camera](Camera.html)
component, just before that Camera performs the culling operation that
determines what it can see. Use `OnPreCull` to execute your own code at this
point in the render loop; for example, you can change the Camera's settings
before performing the culling operation, to affect what the Camera sees.
`OnPreCull` can be a coroutine.  
  
For similar functionality that does not require the script to be on the same
GameObject as a Camera component, see [Camera.onPreCull](Camera-
onPreCull.html). For similar functionality in the Scriptable Render Pipeline,
see [RenderPipelineManager](Rendering.RenderPipelineManager.html).

    
    
    // Attach this to the same [GameObject](GameObject.html) as a [Camera](Camera.html) component.
    // This script inverts the view of the [Camera](Camera.html), so that everything rendered by it is flipped  
      
    using UnityEngine;
    using System.Collections;  
      
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        [Camera](Camera.html) cam;  
      
        void Start()
        {
            cam = GetComponent<[Camera](Camera.html)>();
        }  
      
        void OnPreCull()
        {
            cam.ResetWorldToCameraMatrix();
            cam.ResetProjectionMatrix();
            cam.projectionMatrix = cam.projectionMatrix * [Matrix4x4.Scale](Matrix4x4.Scale.html)(new [Vector3](Vector3.html)(1, -1, 1));
        }  
      
        void OnPreRender()
        {
            [GL.invertCulling](GL-invertCulling.html) = true;
        }  
      
        void OnPostRender()
        {
            [GL.invertCulling](GL-invertCulling.html) = false;
        }
    }
    

Additional resources: [Camera.onPreCull](Camera-onPreCull.html),
[MonoBehaviour.OnPreRender](MonoBehaviour.OnPreRender.html),
[MonoBehaviour.OnPostRender](MonoBehaviour.OnPostRender.html),
[CommandBuffer](Rendering.CommandBuffer.html), [Extending the Built-in Render
Pipeline using CommandBuffers](../Manual/GraphicsCommandBuffers.html).

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

