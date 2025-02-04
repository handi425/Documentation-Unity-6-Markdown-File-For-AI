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

#  [MonoBehaviour](MonoBehaviour.html).OnPreRender()

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
[Camera](Camera.html) renders the scene.

In the Built-in Render Pipeline, Unity calls `OnPreRender` on MonoBehaviours
that are attached to the same GameObject as an enabled [Camera](Camera.html)
component, just before that Camera renders the scene. Use `OnPreRender` to
execute your own code at this point in the render loop; for example, you could
change visual settings to affect the scene while a given Camera is rendering.
`OnPreRender` can be a coroutine.  
  
For similar functionality that does not require the script to be on the same
GameObject as a Camera component, see [Camera.onPreRender](Camera-
onPreRender.html). For similar functionality in the Scriptable Render
Pipeline, see [RenderPipelineManager](Rendering.RenderPipelineManager.html).  
  
Unity calls `OnPreRender` after the Camera performs its culling operation.
This means that if you make a change that affects what the Camera sees, the
change will take effect from the next frame. To make a change to what the
Camera sees in the current frame, use
[MonoBehaviour.OnPreCull](MonoBehaviour.OnPreCull.html).  
  
When Unity calls `OnPreRender`, the Camera's render target and depth textures
are not yet set up. If you need to access these, you can execute code later in
the render loop using a [CommandBuffer](Rendering.CommandBuffer.html).

    
    
    // This script lets you enable/disable fog per camera.
    // by enabling or disabling the script in the title of the Inspector
    // you can turn fog on or off per camera.  
      
    using UnityEngine;
    using System.Collections;  
      
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        private bool revertFogState = false;  
      
        void OnPreRender()
        {
            revertFogState = [RenderSettings.fog](RenderSettings-fog.html);
            [RenderSettings.fog](RenderSettings-fog.html) = enabled;
        }  
      
        void OnPostRender()
        {
            [RenderSettings.fog](RenderSettings-fog.html) = revertFogState;
        }
    }
    

Additional resources: [Camera.onPreRender](Camera-onPreRender.html),
[MonoBehaviour.OnPreCull](MonoBehaviour.OnPreCull.html),
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

