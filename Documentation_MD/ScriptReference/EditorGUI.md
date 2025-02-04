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

# EditorGUI

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

These work pretty much like the normal GUI functions - and also have matching
implementations in [EditorGUILayout](EditorGUILayout.html).

### Static Properties

[actionKey](EditorGUI-actionKey.html)| Is the platform-dependent "action"
modifier key held down? (Read Only)  
---|---  
[indentLevel](EditorGUI-indentLevel.html)| The indent level of the field
labels.  
[showMixedValue](EditorGUI-showMixedValue.html)| Makes the following controls
give the appearance of editing multiple different values.  
  
### Static Methods

[BeginChangeCheck](EditorGUI.BeginChangeCheck.html)| Starts a new code block
to check for GUI changes.  
---|---  
[BeginDisabledGroup](EditorGUI.BeginDisabledGroup.html)| Create a group of
controls that can be disabled.  
[BeginFoldoutHeaderGroup](EditorGUI.BeginFoldoutHeaderGroup.html)| Make a
label with a foldout arrow to the left of it.  
[BeginProperty](EditorGUI.BeginProperty.html)| Create a Property wrapper,
useful for making regular GUI controls work with SerializedProperty.  
[BoundsField](EditorGUI.BoundsField.html)| Makes Center and Extents field for
entering a Bounds.  
[BoundsIntField](EditorGUI.BoundsIntField.html)| Makes Position and Size field
for entering a BoundsInt.  
[ColorField](EditorGUI.ColorField.html)| Makes a field for selecting a Color.  
[CurveField](EditorGUI.CurveField.html)| Makes a field for editing an
AnimationCurve.  
[DelayedDoubleField](EditorGUI.DelayedDoubleField.html)| Makes a delayed text
field for entering doubles.  
[DelayedFloatField](EditorGUI.DelayedFloatField.html)| Makes a delayed text
field for entering floats.  
[DelayedIntField](EditorGUI.DelayedIntField.html)| Makes a delayed text field
for entering integers.  
[DelayedTextField](EditorGUI.DelayedTextField.html)| Makes a delayed text
field.  
[DoubleField](EditorGUI.DoubleField.html)| Makes a text field for entering
doubles.  
[DrawPreviewTexture](EditorGUI.DrawPreviewTexture.html)| Draws the texture
within a rectangle.  
[DrawRect](EditorGUI.DrawRect.html)| Draws a filled rectangle of color at the
specified position and size within the current editor window.  
[DrawTextureAlpha](EditorGUI.DrawTextureAlpha.html)| Draws the alpha channel
of a texture within a rectangle.  
[DropdownButton](EditorGUI.DropdownButton.html)| Makes a button that reacts to
mouse down, for displaying your own dropdown content.  
[DropShadowLabel](EditorGUI.DropShadowLabel.html)| Draws a label with a drop
shadow.  
[EndChangeCheck](EditorGUI.EndChangeCheck.html)| Ends a code block and checks
for any GUI changes.  
[EndDisabledGroup](EditorGUI.EndDisabledGroup.html)| Ends a disabled group
started with BeginDisabledGroup.  
[EndFoldoutHeaderGroup](EditorGUI.EndFoldoutHeaderGroup.html)| Closes a group
started with BeginFoldoutHeaderGroup. Additional resources:
EditorGUILayout.BeginFoldoutHeaderGroup.  
[EndProperty](EditorGUI.EndProperty.html)| Ends a Property wrapper started
with BeginProperty.  
[EnumFlagsField](EditorGUI.EnumFlagsField.html)| Displays a menu with an
option for every value of the enum type when clicked. An option for the value
0 with name "Nothing" and an option for the value ~0 (that is, all bits set)
with the name "Everything" are always displayed at the top of the menu. The
names for the values 0 and ~0 can be overriden by defining these values in the
enum type.  
[EnumPopup](EditorGUI.EnumPopup.html)| Makes an enum popup selection field.  
[FloatField](EditorGUI.FloatField.html)| Makes a text field for entering
floats.  
[FocusTextInControl](EditorGUI.FocusTextInControl.html)| Move keyboard focus
to a named text field and begin editing of the content.  
[Foldout](EditorGUI.Foldout.html)| Makes a label with a foldout arrow to the
left of it.  
[GetPropertyHeight](EditorGUI.GetPropertyHeight.html)| Get the height needed
for a PropertyField control.  
[GradientField](EditorGUI.GradientField.html)| Makes a field for editing a
Gradient.  
[HandlePrefixLabel](EditorGUI.HandlePrefixLabel.html)| Makes a label for some
control.  
[HelpBox](EditorGUI.HelpBox.html)| Makes a help box with a message to the
user.  
[InspectorTitlebar](EditorGUI.InspectorTitlebar.html)| Makes an inspector-
window-like titlebar.  
[IntField](EditorGUI.IntField.html)| Makes a text field for entering integers.  
[IntPopup](EditorGUI.IntPopup.html)| Makes an integer popup selection field.  
[IntSlider](EditorGUI.IntSlider.html)| Makes a slider the user can drag to
change an integer value between a min and a max.  
[LabelField](EditorGUI.LabelField.html)| Makes a label field. (Useful for
showing read-only info.)  
[LargeSplitButtonWithDropdownList](EditorGUI.LargeSplitButtonWithDropdownList.html)|
Creates a large button that contains a regular button section and an arrow to
open a dropdown menu.  
[LayerField](EditorGUI.LayerField.html)| Makes a layer selection field.  
[LinkButton](EditorGUI.LinkButton.html)| Make a clickable link label.  
[LogarithmicIntSlider](EditorGUI.LogarithmicIntSlider.html)| Makes a text
field for entering an integer on a logarithmic scale.  
[LongField](EditorGUI.LongField.html)| Makes a text field for entering long
integers.  
[MaskField](EditorGUI.MaskField.html)| Makes a field for masks.  
[MinMaxSlider](EditorGUI.MinMaxSlider.html)| Makes a special slider the user
can use to specify a range between a min and a max.  
[MultiFloatField](EditorGUI.MultiFloatField.html)| Makes a multi-control with
text fields for entering multiple floats in the same line.  
[MultiIntField](EditorGUI.MultiIntField.html)| Makes a multi-control with text
fields for entering multiple integers in the same line.  
[MultiPropertyField](EditorGUI.MultiPropertyField.html)| Makes a multi-control
with several property fields in the same line.  
[ObjectField](EditorGUI.ObjectField.html)| Makes an object field. You can
assign objects either by drag and drop objects or by selecting an object using
the Object Picker.  
[PasswordField](EditorGUI.PasswordField.html)| Makes a text field where the
user can enter a password.  
[Popup](EditorGUI.Popup.html)| Makes a generic popup selection field.  
[PrefixLabel](EditorGUI.PrefixLabel.html)| Makes a label in front of some
control.  
[ProgressBar](EditorGUI.ProgressBar.html)| Makes a progress bar.  
[PropertyField](EditorGUI.PropertyField.html)| Use this to make a field for a
SerializedProperty in the Editor.  
[RectField](EditorGUI.RectField.html)| Makes an X, Y, W, and H field for
entering a Rect.  
[RectIntField](EditorGUI.RectIntField.html)| Makes an X, Y, W, and H field for
entering a RectInt.  
[RenderingLayerMaskField](EditorGUI.RenderingLayerMaskField.html)| Makes a
rendering layer selection field.  
[SelectableLabel](EditorGUI.SelectableLabel.html)| Makes a selectable label
field. (Useful for showing read-only info that can be copy-pasted.)  
[Slider](EditorGUI.Slider.html)| Makes a slider the user can drag to change a
value between a min and a max.  
[TagField](EditorGUI.TagField.html)| Makes a tag selection field.  
[TextArea](EditorGUI.TextArea.html)| Makes a text area.  
[TextField](EditorGUI.TextField.html)| Makes a text field.  
[Toggle](EditorGUI.Toggle.html)| Makes a toggle.  
[ToggleLeft](EditorGUI.ToggleLeft.html)| Makes a toggle field where the toggle
is to the left and the label immediately to the right of it.  
[Vector2Field](EditorGUI.Vector2Field.html)| Makes an X and Y field for
entering a Vector2.  
[Vector2IntField](EditorGUI.Vector2IntField.html)| Makes an X and Y integer
field for entering a Vector2Int.  
[Vector3Field](EditorGUI.Vector3Field.html)| Makes an X, Y, and Z field for
entering a Vector3.  
[Vector3IntField](EditorGUI.Vector3IntField.html)| Makes an X, Y, and Z
integer field for entering a Vector3Int.  
[Vector4Field](EditorGUI.Vector4Field.html)| Makes an X, Y, Z, and W field for
entering a Vector4.  
  
### Events

[hyperLinkClicked](EditorGUI-hyperLinkClicked.html)| Event used to react on
clicks on a text hyperlink part.  
---|---  
  
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

