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

#
[GraphicsSettings](Rendering.GraphicsSettings.html).UnregisterRenderPipelineSettings

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

**Obsolete** Please use
EditorGraphicsSettings.SetRenderPipelineGlobalSettingsAsset<TRenderPipelineType>(null).
#from(23.2).

## Declaration

public static void UnregisterRenderPipelineSettings();

**Obsolete** Please use
EditorGraphicsSettings.SetRenderPipelineGlobalSettingsAsset(renderPipelineType,
null). #from(23.2).

## Declaration

public static void UnregisterRenderPipelineSettings(Type renderPipelineType);

### Parameters

renderPipelineType | The type of [RenderPipeline](Rendering.RenderPipeline.html).  
---|---  
  
### Description

The method removes the association between the given
[RenderPipeline](Rendering.RenderPipeline.html) and the
[RenderPipelineGlobalSettings](Rendering.RenderPipelineGlobalSettings.html)
asset from GraphicsSettings.

    
    
    using UnityEngine;
    using UnityEngine.Rendering;  
      
    public class ExampleRenderPipelineAsset : [RenderPipelineAsset](Rendering.RenderPipelineAsset.html)
    {
        protected override [RenderPipeline](Rendering.RenderPipeline.html) CreatePipeline()
        {
            return new ExampleRenderPipeline();
        }
    }  
      
    public class ExampleRenderPipeline : [RenderPipeline](Rendering.RenderPipeline.html)
    {
        public ExampleRenderPipeline()
        {
            var mySettings = ExampleRPGlobalSettings.Create();
            ExampleRPGlobalSettings.RegisterToGraphicsSettings(mySettings);
        }  
      
        protected override void Render([ScriptableRenderContext](Rendering.ScriptableRenderContext.html) renderContext, [Camera](Camera.html)[] cameras)
        {
            // Do something
        }  
      
        public virtual [RenderPipelineGlobalSettings](Rendering.RenderPipelineGlobalSettings.html) globalSettings
        {
            get { return ExampleRPGlobalSettings.instance; }
        }  
      
        protected virtual void Dispose(bool disposing)
        {
            ExampleRPGlobalSettings.UnregisterToGraphicsSettings();
        }
    }  
      
    public class ExampleRPGlobalSettings : [RenderPipelineGlobalSettings](Rendering.RenderPipelineGlobalSettings.html)
    {
        private static ExampleRPGlobalSettings cachedInstance = null;
        public static ExampleRPGlobalSettings instance
        {
            get
            {
                if (cachedInstance == null)
                    cachedInstance = [GraphicsSettings.GetSettingsForRenderPipeline](Rendering.GraphicsSettings.GetSettingsForRenderPipeline.html)<ExampleRenderPipeline>() as ExampleRPGlobalSettings;
                return cachedInstance;
            }
        }  
      
        public static void RegisterToGraphicsSettings(ExampleRPGlobalSettings newSettings)
        {
            GraphicsSettings.RegisterRenderPipelineSettings<ExampleRenderPipeline>(newSettings as [RenderPipelineGlobalSettings](Rendering.RenderPipelineGlobalSettings.html));
            cachedInstance = null;
        }  
      
        public static void UnregisterToGraphicsSettings()
        {
            GraphicsSettings.UnregisterRenderPipelineSettings<ExampleRenderPipeline>();
            cachedInstance = null;
        }  
      
        static public ExampleRPGlobalSettings Create()
        {
            ExampleRPGlobalSettings assetCreated = [ScriptableObject.CreateInstance](ScriptableObject.CreateInstance.html)<ExampleRPGlobalSettings>();
            return assetCreated;
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

