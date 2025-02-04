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

# MaterialPropertyDrawer

class in UnityEditor

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

Base class to derive custom material property drawers from.

Use this to create custom UI drawers for your material properties, without
having to write custom [MaterialEditor](MaterialEditor.html) classes. This is
similar to how [PropertyDrawer](PropertyDrawer.html) enables custom UI without
writing custom inspectors.  
  
In shader code, C#-like attribute syntax can be used in front of shader
properties to add drawers to them. Unity has several built-in drawers, and you
can write your own. Here's a shader code snippet demonstrating the syntax:

    
    
              [Shader](Shader.html) "Custom/Example"
    {
        Properties
        {
            _MainTex("Base (RGB)", 2D) = "white" {}  
      
            // [Display](Display.html) a popup with None,Add,Multiply choices,
            // and setup corresponding shader keywords.
            [KeywordEnum(None, Add, Multiply)] _Overlay("[Overlay](Overlays.Overlay.html) mode", Float) = 0  
      
            _OverlayTex("[Overlay](Overlays.Overlay.html)", 2D) = "black" {}  
      
            // [Display](Display.html) as a toggle.
            [[Toggle](UIElements.Toggle.html)] _Invert("Invert color?", Float) = 0
        }  
      
        // rest of shader code...
    }

When implementing your own drawers, you should override OnGUI function. You
can also optionally override GetPropertyHeight and Apply functions. Here's an
example of a property drawer that displays a checkbox for a float property,
with the value set to 0 or 1 depending on the state:

    
    
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);
    using [System](Rendering.VirtualTexturing.System.html);  
      
    // The property drawer class should be placed in an editor script, inside a folder called [Editor](Editor.html).
    // Use with "[MyToggle]" before a float shader property.  
      
    public class MyToggleDrawer : [MaterialPropertyDrawer](MaterialPropertyDrawer.html)
    {
        // Draw the property inside the given rect
        public override void OnGUI ([Rect](Rect.html) position, [MaterialProperty](MaterialProperty.html) prop, String label, [MaterialEditor](MaterialEditor.html) editor)
        {
            // Setup
            bool value = (prop.floatValue != 0.0f);  
      
            [EditorGUI.BeginChangeCheck](EditorGUI.BeginChangeCheck.html)();
            [EditorGUI.showMixedValue](EditorGUI-showMixedValue.html) = prop.hasMixedValue;  
      
            // Show the toggle control
            value = [EditorGUI.Toggle](EditorGUI.Toggle.html)(position, label, value);  
      
            [EditorGUI.showMixedValue](EditorGUI-showMixedValue.html) = false;
            if ([EditorGUI.EndChangeCheck](EditorGUI.EndChangeCheck.html)())
            {
                // Set the new value if it has changed
                prop.floatValue = value ? 1.0f : 0.0f;
            }
        }
    }

The built-in MaterialPropertyDrawers are: ToggleDrawer, ToggleOffDrawer,
KeywordEnumDrawer, EnumDrawer, PowerSliderDrawer, IntRangeDrawer. In shader
code, the "Drawer" suffix of the class name is not written; when Unity
searches for the drawer class it adds "Drawer" automatically.  
  
**Toggle** allows you to enable or disable a single shader keyword. It uses a
float to store the state of the shader keyword, and displays it as a toggle.
When the toggle is enabled, Unity enables the shader keyword; when the toggle
is disabled, Unity disables the shader keyword.  
  
If you specify a keyword name, the toggle affects a shader keyword with that
name. If you don't specify a shader keyword name, the toggle affects a shader
keyword with the name `(uppercase property name)_ON`.

    
    
    // This version specifies a keyword name.
    // The material property name is not important.
    // When the toggle is enabled, Unity enables a shader keyword with the name "ENABLE_EXAMPLE_FEATURE".
    // When the toggle is disabled, Unity disables a shader keyword with the name "ENABLE_EXAMPLE_FEATURE".
    [[Toggle](UIElements.Toggle.html)(ENABLE_EXAMPLE_FEATURE)] _ExampleFeatureEnabled ("Enable example feature", Float) = 0  
      
    // This version does not specify a keyword name.
    // The material property name determines the shader keyword it affects.
    // When this toggle is enabled, Unity enables a shader keyword with the name "_ANOTHER_FEATURE_ON".
    // When this toggle is disabled, Unity disables a shader keyword with the name "_ANOTHER_FEATURE_ON".
    [[Toggle](UIElements.Toggle.html)] _Another_Feature ("Enable another feature", Float) = 0  
      
    // ...Later, in the HLSL code:
    #pragma multi_compile __ ENABLE_EXAMPLE_FEATURE
    #pragma multi_compile __ _ANOTHER_FEATURE_ON
    

**ToggleOff** is similar to **Toggle** , but when the toggle is enabled, Unity
disables the shader keyword; when the toggle is disabled, Unity enables the
shader keyword. Additionally, the default name when you don't specify a shader
keyword name is `(uppercase property name)_OFF`.  
  
`ToggleOff` can be useful for adding functionality and toggles to existing
shaders, while maintaining backwards compatibility.

    
    
    // This version specifies a keyword name.
    // The material property name is not important.
    // When the toggle is enabled, Unity disables a shader keyword with the name "DISABLE_EXAMPLE_FEATURE".
    // When the toggle is disabled, Unity enables a shader keyword with the name "DISABLE_EXAMPLE_FEATURE".
    [ToggleOff(DISABLE_EXAMPLE_FEATURE)] _ExampleFeatureEnabled ("Enable example feature", Float) = 0  
      
    // This version does not specify a keyword name.
    // The material property name determines the shader keyword it affects.
    // When this toggle is enabled, Unity disables a shader keyword with the name "_ANOTHER_FEATURE_OFF".
    // When this toggle is disabled, Unity enables a shader keyword with the name "_ANOTHER_FEATURE_OFF".
    [ToggleOff] _Another_Feature ("Enable another feature", Float) = 0  
      
    // ...Later, in the HLSL code:
    #pragma multi_compile __ DISABLE_EXAMPLE_FEATURE
    #pragma multi_compile __ _ANOTHER_FEATURE_OFF
    

**KeywordEnum** allows you to choose which of a set of shader keywords to
enable. It displays a float as a popup menu, and the value of the float
determines which shader keyword Unity enables. Unity enables a shader keyword
with the name `(uppercase property name)_(uppercase enum value name)`. Up to 9
names can be provided.

    
    
    // [Display](Display.html) a popup with None, Add, Multiply choices.
    // Each option will set _OVERLAY_NONE, _OVERLAY_ADD, _OVERLAY_MULTIPLY shader keywords.
    [KeywordEnum(None, Add, Multiply)] _Overlay ("[Overlay](Overlays.Overlay.html) mode", Float) = 0  
      
    // ...Later, in the HLSL code:
    #pragma multi_compile _OVERLAY_NONE _OVERLAY_ADD _OVERLAY_MULTIPLY
    

**Enum** displays a popup menu for a float property. You can supply either an
enum type name (preferably fully qualified with namespaces, in case there are
multiple types), or explicit name/value pairs to display. Up to 7 name/value
pairs can be specified.

    
    
    // Blend mode values
    [Enum(UnityEngine.Rendering.BlendMode)] _Blend ("Blend mode", Float) = 1  
      
    // A subset of blend mode values, just "One" (value 1) and "SrcAlpha" (value 5).
    [Enum(One,1,SrcAlpha,5)] _Blend2 ("Blend mode subset", Float) = 1

**PowerSlider** displays a slider with a non-linear response for a Range
shader property.

    
    
    // A slider with 3.0 response curve
    [PowerSlider(3.0)] _Shininess ("Shininess", Range (0.01, 1)) = 0.08

**IntRange** displays an integer slider for a Range shader property.

    
    
    // An integer slider for specified range (0 to 255)
    [IntRange] _Alpha ("Alpha", Range (0, 255)) = 100

When a property drawer class name ends with "Decorator", that is a property
decorator, similar to [DecoratorDrawer](DecoratorDrawer.html). They are used
to create headings and dividers between properties that don't affect the
property itself. A single property can have multiple decorators on it. The
built-in decorator drawers are: SpaceDecorator, HeaderDecorator.  
  
**Space** creates vertical space before the shader property.

    
    
    // Default small amount of space.
    [[Space](Space.html)] _Prop1 ("Prop1", Float) = 0  
      
    // Large amount of space.
    [[Space](Space.html)(50)] _Prop2 ("Prop2", Float) = 0

**Header** creates a header text before the shader property.

    
    
    [Header(A group of things)] _Prop1 ("Prop1", Float) = 0

Note that for performance reasons, EditorGUILayout functions are not usable
with MaterialPropertyDrawers.  
  
Additional resources: [MaterialProperty](MaterialProperty.html) class.

### Public Methods

[Apply](MaterialPropertyDrawer.Apply.html)| Apply extra initial values to the
material.  
---|---  
[GetPropertyHeight](MaterialPropertyDrawer.GetPropertyHeight.html)| Override
this method to specify how tall the GUI for this property is in pixels.  
[OnGUI](MaterialPropertyDrawer.OnGUI.html)| Override this method to make your
own GUI for the property.  
  
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

