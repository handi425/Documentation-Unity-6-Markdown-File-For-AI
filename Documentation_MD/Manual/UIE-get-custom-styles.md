[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/UIE-get-custom-styles.html)
  * [中文](/cn/current/Manual/UIE-get-custom-styles.html)
  * [日本語](/ja/current/Manual/UIE-get-custom-styles.html)
  * [한국어](/kr/current/Manual/UIE-get-custom-styles.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/UIE-get-custom-styles.html)
  * [中文](/cn/current/Manual/UIE-get-custom-styles.html)
  * [日本語](/ja/current/Manual/UIE-get-custom-styles.html)
  * [한국어](/kr/current/Manual/UIE-get-custom-styles.html)

  * [Working in Unity](working-in-unity.html)
  * [User interface (UI)](UIToolkits.html)
  * [UI Toolkit](UIElements.html)
  * [Style UI](UIE-USS.html)
  * [USS custom properties (variables)](UIE-USS-variables.html)
  * Get custom styles in C# scripts

[](UIE-uss-built-in-variable-reference.html)

USS built-in variable references

[](UIE-apply-styles-with-csharp.html)

Apply styles in C# scripts

# Get custom styles in C# scripts

You can use the
[`VisualElement.customStyle`](../ScriptReference/UIElements.VisualElement-
customStyle.html) property to get the value of a [custom style property
(variables)](UIE-USS-CustomProperties.html) applied to an element. However,
you can’t directly query it as you would with
[`VisualElement.style`](../ScriptReference/UIElements.VisualElement-
style.html) or
[`VisualElement.resolvedStyle`](../ScriptReference/UIElements.VisualElement-
resolvedStyle.html). Instead, do the following:

  1. Register to the [`CustomStyleResolvedEvent`](../ScriptReference/UIElements.CustomStyleResolvedEvent.html) event.
  2. Call the [`TryGetValues`](../ScriptReference/UIElements.ICustomStyle.TryGetValue.html) method to query the returned object of the `element.customStyle` property.

Assume you have defined a custom style property `--my-custom-color` in USS
like this:

    
    
    .my-selector
    {
        --my-custom-color: red;
    }
    

The following example class shows how to get the value of `--my-custom-color`
applied to an element:

    
    
    public class HasCustomStyleElement : VisualElement
    {
        // Custom style property definition from code indicating the type and the name of the property.
        private static readonly CustomStyleProperty<Color> s_CustomColor = new ("--my-custom-color");
    
        private Color customColor { get; set; }
    
        public HasCustomStyleElement()
        {
            RegisterCallback<CustomStyleResolvedEvent>(OnCustomStyleResolved);
        }
    
        private void OnCustomStyleResolved(CustomStyleResolvedEvent evt)
        {
            // If the custom style property is resolved for this element, you can query its value through the `customStyle` accessor.
            if (evt.customStyle.TryGetValue(s_CustomColor, out var value))
            {
                customColor = value;
            }
            // Otherwise, put some default value.
            else
            {
                customColor = new Color();
            }
        }
    }
    

## Additional resources

  * [Manage UI asset references from C# scripts](UIE-manage-asset-reference.html)
  * [Apply styles with C#](UIE-apply-styles-with-csharp.html)
  * [`customStyle`](../ScriptReference/UIElements.VisualElement-customStyle.html)
  * [`CustomStyleResolvedEvent`](../ScriptReference/UIElements.CustomStyleResolvedEvent.html)
  * [`TryGetValues`](../ScriptReference/UIElements.ICustomStyle.TryGetValue.html)

[](UIE-uss-built-in-variable-reference.html)

USS built-in variable references

[](UIE-apply-styles-with-csharp.html)

Apply styles in C# scripts

Copyright ©2005-2025 Unity Technologies. All rights reserved. Built from
6000.0.36f1 (02b661dc617c). Built on: 2025-01-14.

[Tutorials](https://learn.unity.com/)[Community
Answers](https://answers.unity3d.com)[Knowledge
Base](https://support.unity3d.com/hc/en-
us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-
store)[Terms of
use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy
Policy](https://unity.com/legal/privacy-
policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share
My Personal Information](https://unity.com/legal/do-not-sell-my-personal-
information)

[Your Privacy Choices (Cookie Settings)](javascript:void\(0\);)

