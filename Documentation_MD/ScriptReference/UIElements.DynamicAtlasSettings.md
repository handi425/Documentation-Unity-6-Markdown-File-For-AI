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

# DynamicAtlasSettings

class in UnityEngine.UIElements

/

Implemented
in:[UnityEngine.UIElementsModule](UnityEngine.UIElementsModule.html)

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

Contains the settings used by the dynamic atlas system.

### Static Properties

[defaultFilters](UIElements.DynamicAtlasSettings-defaultFilters.html)|
Default filters for a dynamic atlas.  
---|---  
[defaults](UIElements.DynamicAtlasSettings-defaults.html)|  Specifies default
values used to initialize the structure.  
  
### Properties

[activeFilters](UIElements.DynamicAtlasSettings-activeFilters.html)|  Defines
the filters that the dynamic atlas system uses to exclude textures from the
texture atlas.  
---|---  
[customFilter](UIElements.DynamicAtlasSettings-customFilter.html)|  When a
delegate is assigned, the dynamic atlas system calls it to determine whether
or not a texture can be added to the atlas.  
[maxAtlasSize](UIElements.DynamicAtlasSettings-maxAtlasSize.html)|  Specifies
the maximum size (width/height) of the atlas texture, in pixels. This value
must be a power of two, and must be greater than or equal to minAtlasSize.  
[maxSubTextureSize](UIElements.DynamicAtlasSettings-maxSubTextureSize.html)|
Specifies the maximum size (width/height) of a texture that can be added to
the atlas. When activeFilters contains DynamicAtlasFilters.Size, textures
larger than this size are excluded from the atlas. Otherwise, this value is
not used.  
[minAtlasSize](UIElements.DynamicAtlasSettings-minAtlasSize.html)|  Specifies
the minimum size (width/height) of the atlas texture, in pixels. This value
must be a power of two, and must be greater than 0 and less than or equal to
maxAtlasSize.  
  
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

