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

# ISceneTemplatePipeline

interface in UnityEditor.SceneTemplate

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

### Description

Derive from this interface to package a custom code sequence when a Scene
template is instantiated. ISceneTemplatePipeline is instantiated once when a
template is instantiated, and is notified multiple times during the
instantiation sequence.

    
    
    using UnityEngine.SceneManagement;
    using UnityEditor.SceneTemplate;  
      
    public class MySceneTemplatePipeline : [ISceneTemplatePipeline](SceneTemplate.ISceneTemplatePipeline.html)
    {
        public virtual bool IsValidTemplateForInstantiation([SceneTemplateAsset](SceneTemplate.SceneTemplateAsset.html) sceneTemplateAsset)
        {
            // Check if the scene template is valid for this project.
            return true;
        }  
      
        public virtual void BeforeTemplateInstantiation([SceneTemplateAsset](SceneTemplate.SceneTemplateAsset.html) sceneTemplateAsset, bool isAdditive, string sceneName)
        {
            // Do some work before instantiating the new scene based on the template.
            UnityEngine.Debug.Log($"BeforeTemplateInstantiation {sceneTemplateAsset.name} isAdditive: {isAdditive} sceneName: {sceneName}");
        }  
      
        public virtual void AfterTemplateInstantiation([SceneTemplateAsset](SceneTemplate.SceneTemplateAsset.html) sceneTemplateAsset, [Scene](SceneManagement.Scene.html) scene, bool isAdditive, string sceneName)
        {
            // Do some work after instantiating the new scene.
            UnityEngine.Debug.Log($"AfterTemplateInstantiation {sceneTemplateAsset.name} scene: {scene} isAdditive: {isAdditive} sceneName: {sceneName}");
        }
    }
    

### Public Methods

[AfterTemplateInstantiation](SceneTemplate.ISceneTemplatePipeline.AfterTemplateInstantiation.html)|
An event called after the Scene template is instantiated, and while the new
scene is still loaded.  
---|---  
[BeforeTemplateInstantiation](SceneTemplate.ISceneTemplatePipeline.BeforeTemplateInstantiation.html)|
An event called before the Scene template is instantiated.  
[IsValidTemplateForInstantiation](SceneTemplate.ISceneTemplatePipeline.IsValidTemplateForInstantiation.html)|
An event called before the New Scene dialog is displayed to determine whether
this template is available in the dialog.  
  
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

