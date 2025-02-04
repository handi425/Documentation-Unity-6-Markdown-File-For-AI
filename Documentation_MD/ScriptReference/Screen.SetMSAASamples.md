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

#  [Screen](Screen.html).SetMSAASamples

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

public static void SetMSAASamples(int numSamples);

### Description

Switches the number of MSAA samples of the Unity swapchain.

The value indicates the number of samples per pixel. Valid values are 0 (use
the Quality settings value), 1, 2, 4, and 8. If the graphics API does not
support the value you provide, it uses the next highest supported value. This
function is a low level method that does not affect the rendering state or
settings. It sets the format of the allocated system render target. Unity does
not change the number of samples immediately. The exact time when the change
happens is platform dependent. Calling this method early in the frame might
have an effect during this frame on some platforms, but might defer to the
next frame on other platforms where the switch is done at the end of the
frame.  
  
This function is only available when using a scriptable render pipeline and
will log an error when used with built-in. It enables the render pipeline
internals to control the system rendertarget from script. Setting this from
script will not enable MSAA on the render pipeline. Please see the
renderpipeline documention for information on how to enable MSAA rendering for
the renderpipeline in-use.  
  
If you are writing your own renderpipeline it is likely you want to do your
own resolving as part of your renderpipeline's post processing chain. In that
case, for best performance, it is recommended to set the number of samples to
'1' to disable MSAA on the system render target. If the value is set to 0
(default) the behaviour is identical to built-in, i.e. it uses the msaa sample
count saved in the quality settings and Unity may allocate a MSAA rendertarget
that is not needed since your renderpipeline already resolves as part of it's
post processing.  
  
The example sketches how a renderpipeline may use SetMSAASamples in
combination with it's own MSAA settings to ensure the system render target is
properly configured for it's use case:

    
    
    using UnityEngine;
    using UnityEngine.Rendering;  
      
    [CreateAssetMenu(menuName = "MyRenderPipeline/Create New Pipeline [Asset](VersionControl.Asset.html)")]
    public class MyRenderPipelineAsset : [RenderPipelineAsset](Rendering.RenderPipelineAsset.html)
    {
        public int msaaSamples = 1;
        public bool directToScreen = false;  
      
        protected override [RenderPipeline](Rendering.RenderPipeline.html) CreatePipeline()
        {
            return new MyRenderPipeline(this);
        }
    }  
      
    public class MyRenderPipeline : [RenderPipeline](Rendering.RenderPipeline.html)
    {
        MyRenderPipelineAsset asset;  
      
        public MyRenderPipeline(MyRenderPipelineAsset asset)
        {
            this.asset = asset;
            if (asset.directToScreen)
            {
                [Screen.SetMSAASamples](Screen.SetMSAASamples.html)(asset.msaaSamples);
            }
            else
            {
                [Screen.SetMSAASamples](Screen.SetMSAASamples.html)(1);
            }
        }  
      
        protected override void Render([ScriptableRenderContext](Rendering.ScriptableRenderContext.html) context, [Camera](Camera.html)[] cameras)
        {
            // Render frame, culling shadow maps ...  
      
            // Final output to screen
            if (asset.directToScreen)
            {
                // Render geometry directly to system buffer no post processing is possible
                // the system provies the MSAA resolve as part of the final screen blit or desktop compositor
            }
            else
            {
                // Post processing resolves MSAA and eventually writes single sample data to the sceen
            }
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

