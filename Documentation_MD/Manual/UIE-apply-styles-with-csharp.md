[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/UIE-apply-styles-with-csharp.html)
  * [中文](/cn/current/Manual/UIE-apply-styles-with-csharp.html)
  * [日本語](/ja/current/Manual/UIE-apply-styles-with-csharp.html)
  * [한국어](/kr/current/Manual/UIE-apply-styles-with-csharp.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/UIE-apply-styles-with-csharp.html)
  * [中文](/cn/current/Manual/UIE-apply-styles-with-csharp.html)
  * [日本語](/ja/current/Manual/UIE-apply-styles-with-csharp.html)
  * [한국어](/kr/current/Manual/UIE-apply-styles-with-csharp.html)

  * [Working in Unity](working-in-unity.html)
  * [User interface (UI)](UIToolkits.html)
  * [UI Toolkit](UIElements.html)
  * [Style UI](UIE-USS.html)
  * Apply styles in C# scripts

[](UIE-get-custom-styles.html)

Get custom styles in C# scripts

[](UIE-USS-WritingStyleSheets.html)

Best practices for USS

# Apply styles in C# scripts

You can write to [`style`](../ScriptReference/UIElements.VisualElement-
style.html) to set style values to an element. However, to get the actually
rendered styles of an element, read from
[`resolvedStyle`](../ScriptReference/UIElements.VisualElement-
resolvedStyle.html).

## Set styles

In a C# script, you can set styles directly to the `style` properties of a
**visual element** A node of a visual tree that instantiates or derives from
the C# [`VisualElement`](../ScriptReference/UIElements.VisualElement.html)
class. You can style the look, define the behaviour, and display it on screen
as part of the UI. [More info](UIE-VisualTree.html)  
See in [Glossary](Glossary.html#Visualelement). For example, the following
code sets the background color of a button to red:

    
    
    button.style.backgroundColor = Color.red
    

You can also add a Unity style sheet (USS) to any visual element. Unity
represents USS files as
[`StyleSheet`](../ScriptReference/UIElements.StyleSheet.html) objects in C#
**scripts** A piece of code that allows you to create your own Components,
trigger game events, modify Component properties over time and respond to user
input in any way you like. [More info](creating-scripts.html)  
See in [Glossary](Glossary.html#Scripts).

To add style sheets to a visual element:

  1. Load `StyleSheet` objects with standard Unity APIs, such as `AssetDatabase.Load()` or `Resources.Load()`.
  2. Use the `styleSheets` property of a visual element to add the `StyleSheet` object.

For example, given a style sheet in the local variable `styleSheet` and an
element in the local variable `element`, the following example adds the style
sheet to the element:

    
    
    element.styleSheets.Add(styleSheet);
    

**Note** : Style rules apply to the visual element and all its descendants,
but don’t apply to the parent or siblings of the element. Any change to the
USS file automatically refreshes the **UI**(User Interface) Allows a user to
interact with your application. Unity currently supports three UI systems.
[More info](UI-system-compare.html)  
See in [Glossary](Glossary.html#UI) that uses this style sheet.

## Get resolved styles

Style values on an element are computed from various sources, including
multiple applied classes, inheritance from ancestors, and inline styles from
UXML or C# code. These values might change from frame to frame. The `style`
only holds the inline styles for the element and doesn’t reflect other
sources. The `resolvedStyle` has the final calculated values, considering all
sources on the current frame.

For example, when you use the inline style to set the height for an element,
both the `style` and `resolvedStyle` start with the same value. When the
element is added to the hierarchy, `resolvedStyle.height` can be `NaN` until
the layout updates. If you define the height in a class as a percentage, the
computed width relies on parent properties such as `border-height` and
`padding`. Although `style.height` might give a relative value, such as for
transitions that can change the value, `resolvedStyle.height` gives the actual
rendered height.

To get the resolved style when the geometry changes, you can use the
[`GeometryChangedEvent`](../ScriptReference/UIElements.GeometryChangedEvent.html)
event. This event is triggered when the layout of a VisualElement changes,
which includes changes in size and position. You can register a callback for
this event and in the callback, you can access the resolvedStyle property of
the VisualElement to get the final computed styles.

The following example creates a custom Editor window and logs the resolved
height of an element. The height of the element changes if you resize the
window:

    
    
    using UnityEditor;
    using UnityEngine;
    using UnityEngine.UIElements;
    
    public class ResolvedStyles : EditorWindow
    {
        [MenuItem("Window/UI Toolkit/ResolvedStyles")]
        public static void ShowExample()
        {
            GetWindow<ResolvedStyles>();
        }
        
        private void OnEnable()
        {
            titleContent = new GUIContent("Resolved Styles");
        }
    
        public void CreateGUI()
        {
            VisualElement root = rootVisualElement;
            
            // Element that is tracked.
            // When you resize the Editor window, the inner content is not necessarily updated
            // during the drag operation. The resolved height field is updated whenever the drag
            // operation is complete.
            var element = new VisualElement
            {
                style =
                {
                    flexGrow = 1,
                    backgroundColor = Color.red
                }
            };
            root.Add(element);
    
            // Register a callback for the GeometryChangedEvent
            element.RegisterCallback<GeometryChangedEvent>(OnGeometryChanged);
        }
    
        // Callback for the GeometryChangedEvent
        public void OnGeometryChanged(GeometryChangedEvent evt)
        {
            // Get the VisualElement that triggered the event
            VisualElement element = evt.target as VisualElement;
    
            // Get the resolved style of the VisualElement
            float height = element.resolvedStyle.height;
    
            // Log the resolved of the VisualElement
            Debug.Log("Resolved height: " + height);
        }
    }
    

If the element’s geometry doesn’t change, you can add a scheduler to
periodically check the resolved style of the element:

    
    
    element.schedule.Execute(() =>
    {
        Debug.Log(element.resolvedStyle.height);
    }).Every(100);
    

## Additional resources

  * [Manage UI asset references from C# scripts](UIE-manage-asset-reference.html)
  * [Get custom styles](UIE-get-custom-styles.html)

[](UIE-get-custom-styles.html)

Get custom styles in C# scripts

[](UIE-USS-WritingStyleSheets.html)

Best practices for USS

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

