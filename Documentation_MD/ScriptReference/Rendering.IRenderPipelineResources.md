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

# IRenderPipelineResources

interface in UnityEngine.Rendering

Leave feedback

  

Implements
interfaces:[IRenderPipelineGraphicsSettings](Rendering.IRenderPipelineGraphicsSettings.html)

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

### Description

Classes implementing this interface contain the resources required for your
graphic features to work.

Classes implementing this interface will contain all the resources that are
mandatory for your Render Pipeline to work. There is a mechanism that allows
to set up null fields for you based on
[ResourcePathAttribute](Rendering.ResourcePathAttribute.html) attribute. When
the resource is created, a loading mechanism is called to make sure your
resources are not created with null values. It is only called automatically at
creation.  
  
See also ResourceContainerAttribute.

    
    
    using UnityEngine;
    using UnityEngine.Rendering;
    using [System](Rendering.VirtualTexturing.System.html);  
      
    [Serializable]
    [SupportedOnRenderPipeline(typeof(DummyPipelineAsset))]
    class MyResourceForFeatureX : [IRenderPipelineResources](Rendering.IRenderPipelineResources.html)
    {
        enum Version
        {
            Initial,
            ChangedIcon1,
            ChangedShader,
            
            Count,
            Last = Count - 1
        }
        [[SerializeField](SerializeField.html), [HideInInspector](HideInInspector.html)] Version m_version = Version.Last;
        public int version => (int)m_version;  
      
        [ResourcePath("ResourceAssets/resourceIcon1.png")]
        public [Texture2D](Texture2D.html) icon1;
        [ResourcePath("ResourceAssets/resourceIcon2.png")]
        public [Texture2D](Texture2D.html) icon2;
        [ResourcePath("My/[Shader](Shader.html)/Path", ResourcePathAttribute.SearchType.ShaderName)]
        public [Shader](Shader.html) shader;
    }
    

Here we add a MyResourceForFeatureX that contains various icons and shader for
a rendering feature. With the SupportedOn, we only add it for the SRP
Universal Render Pipeline. Feel free to replace it by your own pipeline or
HDRenderPipelineAsset if you use them.

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

