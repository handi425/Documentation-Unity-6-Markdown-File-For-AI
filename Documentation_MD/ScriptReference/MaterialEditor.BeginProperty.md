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

#  [MaterialEditor](MaterialEditor.html).BeginProperty

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

public static void BeginProperty([MaterialProperty](MaterialProperty.html)
property);

## Declaration

public static void BeginProperty([Rect](Rect.html) rect,
[MaterialProperty](MaterialProperty.html) property);

## Declaration

public static void BeginProperty([SerializedProperty](SerializedProperty.html)
property);

## Declaration

public static void BeginProperty([Rect](Rect.html) rect,
[SerializedProperty](SerializedProperty.html) property);

### Parameters

rect | The box which encloses the GUI control. May include a label.  
---|---  
property | The property this GUI control modifies.  
  
### Description

Creates a wrapper enabling the Unity Editor to display GUI controls for the
property.

The [MaterialEditor](MaterialEditor.html) has methods that display specific
Material Properties such as
[MaterialEditor.ShaderProperty](MaterialEditor.ShaderProperty.html), or
[MaterialEditor.TextureProperty](MaterialEditor.TextureProperty.html).  
  
However, if you display a Property with a GUI control (such as
[EditorGUI.Toggle](EditorGUI.Toggle.html)) instead of one of these methods,
you can use a property wrapper to configure the visual presentation of this
Property. Using a property wrapper enables you to display MaterialVariant
overrides in a bold font, provide access to the Apply/Revert options via a
right-click menu, disable the GUI for locked Properties, and set the
appearance when editing multiple different values.  
  
Property wrappers begin with BeginProperty and end with
[MaterialEditor.EndProperty](MaterialEditor.EndProperty.html). If you do not
provide a rect parameter, the Editor tries to determine one by calling
[GUILayoutUtility.GetLastRect](GUILayoutUtility.GetLastRect.html) at the end
of the scope.  
  
If you use a custom method to display [Material.renderQueue](Material-
renderQueue.html), [Material.doubleSidedGI](Material-doubleSidedGI.html),
[Material.enableInstancing](Material-enableInstancing.html) or
[Material.globalIlluminationFlags](Material-globalIlluminationFlags.html), you
can create a property wrapper around the field by using the corresponding
[SerializedProperty](SerializedProperty.html).  
  
Additional resources:
[MaterialEditor.ShaderProperty](MaterialEditor.ShaderProperty.html),
[SerializedProperty](SerializedProperty.html),
[MaterialEditor.EndProperty](MaterialEditor.EndProperty.html).

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

