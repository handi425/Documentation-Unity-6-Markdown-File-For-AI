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

# CustomBinding

class in UnityEngine.UIElements

/

Inherits from:[UIElements.Binding](UIElements.Binding.html)

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

Base class for general purpose binding extensibility.

The following example creates a custom binding that displays the current time.
You can bind it to the text field of a Label to create a clock.

    
    
    using [System](Rendering.VirtualTexturing.System.html);
    using Unity.Properties;
    using UnityEngine.UIElements;  
      
    [UxmlObject]
    public partial class CurrentTimeBinding : [CustomBinding](UIElements.CustomBinding.html)
    {
        [UxmlAttribute]
        public string timeFormat = "HH:mm:ss";  
      
        public CurrentTimeBinding()
        {
            updateTrigger = [BindingUpdateTrigger.EveryUpdate](UIElements.BindingUpdateTrigger.EveryUpdate.html);
        }  
      
        protected override [BindingResult](UIElements.BindingResult.html) [Update](PlayerLoop.Update.html)(in [BindingContext](UIElements.BindingContext.html) context)
        {
            var timeNow = DateTime.Now.ToString(timeFormat);
            var element = context.targetElement;
            if ([ConverterGroups.TrySetValueGlobal](UIElements.ConverterGroups.TrySetValueGlobal.html)(ref element, context.bindingId, timeNow, out var errorCode))
                return new [BindingResult](UIElements.BindingResult.html)([BindingStatus.Success](UIElements.BindingStatus.Success.html));  
      
            // [Error](PackageManager.Error.html) handling
            var bindingTypename = [TypeUtility.GetTypeDisplayName](Unity.Properties.TypeUtility.GetTypeDisplayName.html)(typeof(CurrentTimeBinding));
            var bindingId = $"{[TypeUtility.GetTypeDisplayName](Unity.Properties.TypeUtility.GetTypeDisplayName.html)(element.GetType())}.{context.bindingId}";  
      
            return errorCode switch
            {
                [VisitReturnCode.InvalidPath](Unity.Properties.VisitReturnCode.InvalidPath.html) => new [BindingResult](UIElements.BindingResult.html)([BindingStatus.Failure](UIElements.BindingStatus.Failure.html), $"{bindingTypename}: [Binding](UIElements.Binding.html) id `{bindingId}` is either invalid or contains a `null` value."),
                [VisitReturnCode.InvalidCast](Unity.Properties.VisitReturnCode.InvalidCast.html) => new [BindingResult](UIElements.BindingResult.html)([BindingStatus.Failure](UIElements.BindingStatus.Failure.html), $"{bindingTypename}: Invalid conversion from `string` for binding id `{bindingId}`"),
                [VisitReturnCode.AccessViolation](Unity.Properties.VisitReturnCode.AccessViolation.html) => new [BindingResult](UIElements.BindingResult.html)([BindingStatus.Failure](UIElements.BindingStatus.Failure.html), $"{bindingTypename}: Trying set value for binding id `{bindingId}`, but it is read-only."),
                _ => throw new ArgumentOutOfRangeException()
            };
        }
    }
    

### Public Methods

[Update](UIElements.CustomBinding.Update.html)|  Called when the binding
system updates the binding.  
---|---  
  
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

