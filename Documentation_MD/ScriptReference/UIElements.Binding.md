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

# Binding

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

Base class for defining a binding.

### Properties

[isDirty](UIElements.Binding-isDirty.html)|  When set to true, the binding
instance updates during the next update cycle. When set to false, the binding
instance updates only if a change is detected.  
---|---  
[updateTrigger](UIElements.Binding-updateTrigger.html)|  When set to
BindingUpdateTrigger.EveryUpdate, the binding instance updates in every
update, regardless of the data source version.  
  
### Public Methods

[MarkDirty](UIElements.Binding.MarkDirty.html)|  Notifies the binding system
to process this binding.  
---|---  
[OnActivated](UIElements.Binding.OnActivated.html)|  Called when the binding
becomes active for a specific VisualElement.  
[OnDataSourceChanged](UIElements.Binding.OnDataSourceChanged.html)|  Called
when the resolved data source of a binding changes.  
[OnDeactivated](UIElements.Binding.OnDeactivated.html)|  Called when the
binding is no longer active for a specific VisualElement.  
  
### Static Methods

[ResetPanelLogLevel](UIElements.Binding.ResetPanelLogLevel.html)|  Resets the
log level for binding failures on a panel to use the global setting.  
---|---  
[SetGlobalLogLevel](UIElements.Binding.SetGlobalLogLevel.html)|  Sets the log
level for all binding failures.  
[SetPanelLogLevel](UIElements.Binding.SetPanelLogLevel.html)|  Sets the log
level for binding failures on a panel.  
  
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

