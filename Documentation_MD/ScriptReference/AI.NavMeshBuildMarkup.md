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

# NavMeshBuildMarkup

struct in UnityEngine.AI

/

Implemented in:[UnityEngine.AIModule](UnityEngine.AIModule.html)

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

The NavMesh build markup allows you to control how certain objects are treated
during the NavMesh build process, specifically when collecting sources for
building.

You can override the area type or specify that certain objects should be
excluded from collected sources. The markup can be applied hierarchically or
to only the specified object. Additional resources:
[NavMeshBuilder.CollectSources](AI.NavMeshBuilder.CollectSources.html).

### Properties

[applyToChildren](AI.NavMeshBuildMarkup-applyToChildren.html)| Use this to
specify if the GameObject's children also use these markup settings.  
---|---  
[area](AI.NavMeshBuildMarkup-area.html)| The area type to use when override
area is enabled.  
[generateLinks](AI.NavMeshBuildMarkup-generateLinks.html)| Use this to specify
whether the GameObject and its children should be included in the link
generation process.  
[ignoreFromBuild](AI.NavMeshBuildMarkup-ignoreFromBuild.html)| Use this to
specify whether the GameObject and its children should be ignored.  
[overrideArea](AI.NavMeshBuildMarkup-overrideArea.html)| Use this to specify
whether the area type of the GameObject and its children should be overridden
by the area type specified in this struct.  
[overrideGenerateLinks](AI.NavMeshBuildMarkup-overrideGenerateLinks.html)| Use
this to specify whether the default links generation condition for the
GameObject and its children should be overridden by the generateLinks option
specified in this struct.  
[overrideIgnore](AI.NavMeshBuildMarkup-overrideIgnore.html)| Set this to true
in order to enable the ignoreFromBuild property.  
[root](AI.NavMeshBuildMarkup-root.html)| Use this to specify which GameObject
(including the GameObject’s children) the markup should be applied to.  
  
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

