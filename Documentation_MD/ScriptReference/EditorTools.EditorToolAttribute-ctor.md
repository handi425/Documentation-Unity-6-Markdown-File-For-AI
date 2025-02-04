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

# EditorToolAttribute Constructor

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

public EditorToolAttribute(string displayName, Type componentToolTarget, Type
editorToolContext);

## Declaration

public EditorToolAttribute(string displayName, Type componentToolTarget);

## Declaration

public EditorToolAttribute(string displayName, Type componentToolTarget, Type
editorToolContext, Type variantGroup);

## Declaration

public EditorToolAttribute(string displayName, Type componentToolTarget, Type
editorToolContext, int toolPriority, Type variantGroup);

## Declaration

public EditorToolAttribute(string displayName, Type componentToolTarget, Type
editorToolContext, int toolPriority, Type variantGroup, int variantPriority);

### Parameters

displayName | The name to display in menus.  
---|---  
componentToolTarget | The type this tool can edit. Set to null if the tool is not a [Component](Component.html) tool.  
editorToolContext | The [EditorToolContext](EditorTools.EditorToolContext.html) type that this tool relates to. When an [EditorTool](EditorTools.EditorTool.html) defines an `editorToolContext` scope, the tool is not shown in menus and must be activated by the [EditorToolContext.ResolveTool](EditorTools.EditorToolContext.ResolveTool.html) method.  
toolPriority | The order to display tools in the Tools overlay in. Refer to [ToolAttribute.toolPriority](EditorTools.ToolAttribute-toolPriority.html).  
variantGroup | The tool variant group to assign the tool to in the Tools overlay. Tool variants are used to group similar tools into a single button in the Tools overlay. Refer to [ToolAttribute.variantGroup](EditorTools.ToolAttribute-variantGroup.html).  
variantPriority | The variant priority defines the order that tools are displayed in when they are displayed in a [ToolAttribute.variantGroup](EditorTools.ToolAttribute-variantGroup.html) dropdown.  
  
### Description

Registers an [EditorTool](EditorTools.EditorTool.html) as either a Global tool
or a [CustomEditor](CustomEditor.html) tool.

A Global tool is always available in the toolbar menu. A
[CustomEditor](CustomEditor.html) tool is only available when the current
selection contains a matching target type.

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

