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

# DataBinding

class in UnityEngine.UIElements

/

Inherits from:[UIElements.Binding](UIElements.Binding.html)

/

Implemented
in:[UnityEngine.UIElementsModule](UnityEngine.UIElementsModule.html)

Leave feedback

  

Implements
interfaces:[IDataSourceProvider](UIElements.IDataSourceProvider.html)

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

Binding type that enables data synchronization between a property of a data
source and a property of a [VisualElement](UIElements.VisualElement.html).

### Properties

[bindingMode](UIElements.DataBinding-bindingMode.html)|  Controls how this
binding should be updated. The default value is BindingMode.TwoWay.  
---|---  
[dataSource](UIElements.DataBinding-dataSource.html)|  Object that serves as a
local source for the binding, and is particularly useful when the data source
is not part of the UI hierarchy, such as a static localization table. If this
object is null, the binding resolves the data source using its normal
resolution method.  
[dataSourcePath](UIElements.DataBinding-dataSourcePath.html)|  Path from the
data source to the value.  
[dataSourceType](UIElements.DataBinding-dataSourceType.html)|  The possible
data source types that can be assigned to the binding.  
[sourceToUiConverters](UIElements.DataBinding-sourceToUiConverters.html)|
Returns the ConverterGroup used when trying to convert data from the data
source to a UI property.  
[uiToSourceConverters](UIElements.DataBinding-uiToSourceConverters.html)|
Returns the ConverterGroup used when trying to convert data from a UI property
back to the data source.  
  
### Constructors

[DataBinding](UIElements.DataBinding-ctor.html)|  Initializes and returns an
instance of DataBinding.  
---|---  
  
### Public Methods

[ApplyConverterGroupToSource](UIElements.DataBinding.ApplyConverterGroupToSource.html)|
Applies a ConverterGroup to this binding that will be used when converting
data between a UI control to a data source.  
---|---  
[ApplyConverterGroupToUI](UIElements.DataBinding.ApplyConverterGroupToUI.html)|
Applies a ConverterGroup to this binding that will be used when converting
data between a data source to a UI control.  
[UpdateSource](UIElements.DataBinding.UpdateSource.html)|  Callback called to
allow derived classes to update the data source with the resolved value when a
change from the UI is detected.  
[UpdateUI](UIElements.DataBinding.UpdateUI.html)|  Callback called to allow
derived classes to update the UI with the resolved value from the data source.  
  
### Inherited Members

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

