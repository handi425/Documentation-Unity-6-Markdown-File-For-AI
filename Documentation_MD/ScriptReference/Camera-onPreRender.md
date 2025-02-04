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

#  [Camera](Camera.html).onPreRender

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

public static [Camera.CameraCallback](Camera.CameraCallback.html) onPreRender;

### Description

Delegate that you can use to execute custom code before a
[Camera](Camera.html) renders the scene.

In the Built-in Render Pipeline, Unity calls this `onPreRender` before any
Camera begins rendering. To execute custom code at this point, create
callbacks that match the signature of
[CameraCallback](Camera.CameraCallback.html), and add them to this delegate.  
  
For similar functionality that applies only to a single Camera and requires
your script to be on the same GameObject, see
[MonoBehaviour.OnPreRender](MonoBehaviour.OnPreRender.html).  
  
If you're using a Scriptable Render Pipeline, for example the Universal Render
Pipeline, use [RenderPipelineManager](Rendering.RenderPipelineManager.html)
instead.  
  
Unity calls `onPreRender` after the Camera performs its culling operation.
This means that if you make a change that affects what the Camera sees, the
change will take effect from the next frame. To make a change to what the
Camera sees in the current frame, use [Camera.onPreCull](Camera-
onPreCull.html).  
  
When Unity calls `onPreRender`, the Camera's render target and depth textures
are not yet set up. If you need to access these, you can execute code later in
the render loop using a [CommandBuffer](Rendering.CommandBuffer.html).

    
    
    using UnityEngine;  
      
    public class CameraCallbackExample : [MonoBehaviour](MonoBehaviour.html)
    {
        // Add your callback to the delegate's invocation list
        void Start()
        {
            [Camera.onPreRender](Camera-onPreRender.html) += OnPreRenderCallback;
        }  
      
        // Unity calls the methods in this delegate's invocation list before rendering any camera
        void OnPreRenderCallback([Camera](Camera.html) cam)
        {
            [Debug.Log](Debug.Log.html)("[Camera](Camera.html) callback: [Camera](Camera.html) name is " + cam.name);  
      
            // Unity calls this for every active [Camera](Camera.html).
            // If you're only interested in a particular [Camera](Camera.html),
            // check whether the [Camera](Camera.html) is the one you're interested in
            if (cam == [Camera.main](Camera-main.html))
            {
                // Put your custom code here
            }
        }  
      
        // Remove your callback from the delegate's invocation list
        void OnDestroy()
        {
            [Camera.onPreRender](Camera-onPreRender.html) -= OnPreRenderCallback;
        }
    }
    

Additional resources: [CameraCallback](Camera.CameraCallback.html),
[Camera.onPreCull](Camera-onPreCull.html), [Camera.onPostRender](Camera-
onPostRender.html),
[MonoBehaviour.OnPreRender](MonoBehaviour.OnPreRender.html),
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

