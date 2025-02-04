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

# ToolAttribute

class in UnityEditor.EditorTools

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

Base class from which
[EditorToolAttribute](EditorTools.EditorToolAttribute.html) and
[EditorToolContextAttribute](EditorTools.EditorToolContextAttribute.html)
inherit.

### Static Properties

[defaultPriority](EditorTools.ToolAttribute-defaultPriority.html)| The default
value for ToolAttribute.toolPriority and ToolAttribute.variantPriority.
Specify a priority lower than this value to display a tool before the default
entries, or specify a higher value to display it after the default entries.  
---|---  
  
### Properties

[displayName](EditorTools.ToolAttribute-displayName.html)| The name that
displays in menus.  
---|---  
[targetContext](EditorTools.ToolAttribute-targetContext.html)| If provided,
the EditorTool will only be made available when the
ToolManager.activeContextType is equal to targetContext.  
[targetType](EditorTools.ToolAttribute-targetType.html)| Set to the type that
this EditorTool or EditorToolContext can edit. Set to null if the tool is not
specific to a Component and should be available at any time.  
[toolPriority](EditorTools.ToolAttribute-toolPriority.html)| Tool priority
defines the order that tools are displayed in within the Tools Overlay.  
[variantGroup](EditorTools.ToolAttribute-variantGroup.html)| Tool variants are
used to group logically similar tools into a single button in the Tools
Overlay.  
[variantPriority](EditorTools.ToolAttribute-variantPriority.html)| The variant
priority defines the order that tools are displayed in when they are displayed
in a ToolAttribute.variantGroup dropdown.  
  
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

