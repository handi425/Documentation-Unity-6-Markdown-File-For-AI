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

# TextInputBaseField<T0>

class in UnityEngine.UIElements

/

Inherits from:[UIElements.BaseField_1](UIElements.BaseField_1.html)

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

Abstract base class used for all text-based fields.

### Static Properties

[inputUssClassName](UIElements.TextInputBaseField_1-inputUssClassName.html)|
USS class name of input elements in elements of this type.  
---|---  
[labelUssClassName](UIElements.TextInputBaseField_1-labelUssClassName.html)|
USS class name of labels in elements of this type.  
[multilineInputUssClassName](UIElements.TextInputBaseField_1-multilineInputUssClassName.html)|
USS class name of multiline input elements in elements of this type.  
[placeholderUssClassName](UIElements.TextInputBaseField_1-placeholderUssClassName.html)|
USS class name of input elements when placeholder text is shown  
[singleLineInputUssClassName](UIElements.TextInputBaseField_1-singleLineInputUssClassName.html)|
USS class name of single line input elements in elements of this type.  
[textInputUssName](UIElements.TextInputBaseField_1-textInputUssName.html)|
USS class name of input elements in elements of this type.  
[ussClassName](UIElements.TextInputBaseField_1-ussClassName.html)|  USS class
name of elements of this type.  
  
### Properties

[autoCorrection](UIElements.TextInputBaseField_1-autoCorrection.html)|
Determines if the touch screen keyboard auto correction is turned on or off.  
---|---  
[cursorColor](UIElements.TextInputBaseField_1-cursorColor.html)|  Color of the
cursor.  
[cursorIndex](UIElements.TextInputBaseField_1-cursorIndex.html)|  This is the
cursor index in the text presented.  
[cursorPosition](UIElements.TextInputBaseField_1-cursorPosition.html)|  The
position of the text cursor inside the element.  
[doubleClickSelectsWord](UIElements.TextInputBaseField_1-doubleClickSelectsWord.html)|
Controls whether double clicking selects the word under the mouse pointer or
not.  
[emojiFallbackSupport](UIElements.TextInputBaseField_1-emojiFallbackSupport.html)|
Specifies the order in which the system should look for Emoji characters when
rendering text. If this setting is enabled, the global Emoji Fallback list
will be searched first for characters defined as Emoji in the Unicode 14.0
standard.  
[hideMobileInput](UIElements.TextInputBaseField_1-hideMobileInput.html)|
Hides or shows the mobile input field.  
[isDelayed](UIElements.TextInputBaseField_1-isDelayed.html)|  If set to true,
the value property isn't updated until either the user presses Enter or the
text field loses focus.  
[isPasswordField](UIElements.TextInputBaseField_1-isPasswordField.html)|
Returns true if the field is used to edit a password.  
[isReadOnly](UIElements.TextInputBaseField_1-isReadOnly.html)|  Returns true
if the field is read only.  
[keyboardType](UIElements.TextInputBaseField_1-keyboardType.html)|  The type
of mobile keyboard that will be used.  
[maskChar](UIElements.TextInputBaseField_1-maskChar.html)|  The character used
for masking in a password field.  
[maxLength](UIElements.TextInputBaseField_1-maxLength.html)|  Maximum number
of characters for the field.  
[onIsReadOnlyChanged](UIElements.TextInputBaseField_1-onIsReadOnlyChanged.html)|
Calls the methods in its invocation list when isReadOnly changes.  
[selectAllOnFocus](UIElements.TextInputBaseField_1-selectAllOnFocus.html)|
Controls whether the element's content is selected upon receiving focus.  
[selectAllOnMouseUp](UIElements.TextInputBaseField_1-selectAllOnMouseUp.html)|
Controls whether the element's content is selected when you mouse up for the
first time.  
[selectIndex](UIElements.TextInputBaseField_1-selectIndex.html)|  This is the
selection index in the text presented.  
[selectionColor](UIElements.TextInputBaseField_1-selectionColor.html)|
Background color of selected text.  
[text](UIElements.TextInputBaseField_1-text.html)|  The value of the input
field.  
[textEdition](UIElements.TextInputBaseField_1-textEdition.html)|  Retrieves
this Field's TextElement ITextEdition  
[textSelection](UIElements.TextInputBaseField_1-textSelection.html)|
Retrieves this Field's TextElement ITextSelection  
[touchScreenKeyboard](UIElements.TextInputBaseField_1-touchScreenKeyboard.html)|
The active touch keyboard being displayed.  
[tripleClickSelectsLine](UIElements.TextInputBaseField_1-tripleClickSelectsLine.html)|
Controls whether triple clicking selects the entire line under the mouse
pointer or not.  
[verticalScrollerVisibility](UIElements.TextInputBaseField_1-verticalScrollerVisibility.html)|
Option for controlling the visibility of the vertical scroll bar in the
TextInputBaseField_1.  
  
### Public Methods

[MeasureTextSize](UIElements.TextInputBaseField_1.MeasureTextSize.html)|
Computes the size needed to display a text string based on element style
values such as font, font-size, and word-wrap.  
---|---  
[SelectAll](UIElements.TextInputBaseField_1.SelectAll.html)|  Selects all the
text contained in the field.  
[SelectNone](UIElements.TextInputBaseField_1.SelectNone.html)|  Remove
selection  
[SelectRange](UIElements.TextInputBaseField_1.SelectRange.html)|  Select text
between cursorIndex and selectIndex.  
  
### Protected Methods

[StringToValue](UIElements.TextInputBaseField_1.StringToValue.html)|  Converts
a string to the value of the specified generic type from the subclass.  
---|---  
[ValueToString](UIElements.TextInputBaseField_1.ValueToString.html)|  Converts
a value of the specified generic type from the subclass to a string
representation.  
  
### Inherited Members

### Static Properties

[alignedFieldUssClassName](UIElements.BaseField_1-alignedFieldUssClassName.html)|
USS class name of elements that are aligned in a inspector element  
---|---  
[inputUssClassName](UIElements.BaseField_1-inputUssClassName.html)|  USS class
name of input elements in elements of this type.  
[labelDraggerVariantUssClassName](UIElements.BaseField_1-labelDraggerVariantUssClassName.html)|
USS class name of labels in elements of this type, when there is a dragger
attached on them.  
[labelUssClassName](UIElements.BaseField_1-labelUssClassName.html)|  USS class
name of labels in elements of this type.  
[mixedValueLabelUssClassName](UIElements.BaseField_1-mixedValueLabelUssClassName.html)|
USS class name of elements that show mixed values  
[noLabelVariantUssClassName](UIElements.BaseField_1-noLabelVariantUssClassName.html)|
USS class name of elements of this type, when there is no label.  
[ussClassName](UIElements.BaseField_1-ussClassName.html)|  USS class name of
elements of this type.  
[disabledUssClassName](UIElements.VisualElement-disabledUssClassName.html)|
USS class name of local disabled elements.  
  
### Properties

[label](UIElements.BaseField_1-label.html)|  The string representing the label
that will appear beside the field.  
---|---  
[labelElement](UIElements.BaseField_1-labelElement.html)|  This is the Label
object that appears beside the input for the field.  
[mixedValueLabel](UIElements.BaseField_1-mixedValueLabel.html)|  Read-only
label used to give the appearance of editing multiple different values.  
[rawValue](UIElements.BaseField_1-rawValue.html)|  The value of the element.  
[showMixedValue](UIElements.BaseField_1-showMixedValue.html)|  When set to
true, gives the field the appearance of editing multiple different values.  
[value](UIElements.BaseField_1-value.html)|  The value associated with the
field.  
[binding](UIElements.BindableElement-binding.html)|  Binding object that will
be updated.  
[bindingPath](UIElements.BindableElement-bindingPath.html)|  Path of the
target property to be bound.  
[canGrabFocus](UIElements.Focusable-canGrabFocus.html)|  Return true if the
element can be focused.  
[delegatesFocus](UIElements.Focusable-delegatesFocus.html)|  Whether the
element should delegate the focus to its children.  
[focusable](UIElements.Focusable-focusable.html)|  True if the element can be
focused.  
[focusController](UIElements.Focusable-focusController.html)|  Return the
focus controller for this element.  
[tabIndex](UIElements.Focusable-tabIndex.html)|  An integer used to sort
focusables in the focus ring. Must be greater than or equal to zero.  
[childCount](UIElements.VisualElement-childCount.html)|  Number of child
elements in this object's contentContainer.  
[contentContainer](UIElements.VisualElement-contentContainer.html)|  Child
elements are added to it, usually this is the same as the element itself.  
[contentRect](UIElements.VisualElement-contentRect.html)|  The rectangle of
the content area of the element, in the local space of the element. (Read
Only)  
[customStyle](UIElements.VisualElement-customStyle.html)|  The custom style
properties accessor of a VisualElement (Read Only).  
[dataSource](UIElements.VisualElement-dataSource.html)|  Assigns a data source
to this VisualElement which overrides any inherited data source. This data
source is inherited by all children.  
[dataSourcePath](UIElements.VisualElement-dataSourcePath.html)|  Path from the
data source to the value.  
[dataSourceType](UIElements.VisualElement-dataSourceType.html)|  The possible
type of data source assignable to this VisualElement. This information is only
used by the UI Builder as a hint to provide some completion to the data source
path field when the effective data source cannot be specified at design time.  
[disablePlayModeTint](UIElements.VisualElement-disablePlayModeTint.html)|
Play-mode tint is applied by default unless this is set to true. It's applied
hierarchically to this VisualElement and to all its children that exist on an
editor panel.  
[enabledInHierarchy](UIElements.VisualElement-enabledInHierarchy.html)|
Returns true if the VisualElement is enabled in its own hierarchy.  
[enabledSelf](UIElements.VisualElement-enabledSelf.html)|  Returns true if the
VisualElement is enabled locally.  
[experimental](UIElements.VisualElement-experimental.html)|  Returns the
UIElements experimental interfaces.  
[generateVisualContent](UIElements.VisualElement-generateVisualContent.html)|
Delegate function to generate the visual content of a visual element.  
[hierarchy](UIElements.VisualElement-hierarchy.html)|  Access to this element
physical hierarchy  
[languageDirection](UIElements.VisualElement-languageDirection.html)|
Indicates the directionality of the element's text. The value will propagate
to the element's children.  
[layout](UIElements.VisualElement-layout.html)|  The position and size of the
VisualElement relative to its parent, as computed by the layout system. (Read
Only)  
[localBound](UIElements.VisualElement-localBound.html)|  Returns a Rect
representing the Axis-aligned Bounding Box (AABB) after applying the
transform, but before applying the layout translation.  
[name](UIElements.VisualElement-name.html)|  The name of this VisualElement.  
[paddingRect](UIElements.VisualElement-paddingRect.html)|  The rectangle of
the padding area of the element, in the local space of the element.  
[panel](UIElements.VisualElement-panel.html)|  The panel onto which this
VisualElement is attached.  
[parent](UIElements.VisualElement-parent.html)|  The parent of this
VisualElement.  
[pickingMode](UIElements.VisualElement-pickingMode.html)|  Determines if this
element can be pick during mouseEvents or IPanel.Pick queries.  
[resolvedStyle](UIElements.VisualElement-resolvedStyle.html)|  The final
rendered style values of a visual element, as it's rendered in the current
frame.(Read Only)  
[scaledPixelsPerPoint](UIElements.VisualElement-scaledPixelsPerPoint.html)|
Return the resulting scaling from the panel that considers the screen DPI and
the customizable scaling factor, but not the transform scale of the element
and its ancestors. See Panel.scaledPixelsPerPoint. This should only be called
on elements that are part of a panel.  
[schedule](UIElements.VisualElement-schedule.html)|  Retrieves this
VisualElement's IVisualElementScheduler  
[style](UIElements.VisualElement-style.html)|  Sets the style values on a
VisualElement.  
[styleSheets](UIElements.VisualElement-styleSheets.html)|  Returns a
VisualElementStyleSheetSet that manipulates style sheets attached to this
element.  
[this[int]](UIElements.VisualElement.Index_operator.html)|  Retrieves the
child element at a specific index.  
[tooltip](UIElements.VisualElement-tooltip.html)|  Text to display inside an
information box after the user hovers the element for a small amount of time.
This is only supported in the Editor UI.  
[transform](UIElements.VisualElement-transform.html)|  Returns a transform
object for this VisualElement. ITransform  
[usageHints](UIElements.VisualElement-usageHints.html)|  A combination of hint
values that specify high-level intended usage patterns for the VisualElement.
This property can only be set when the VisualElement is not yet part of a
Panel. Once part of a Panel, this property becomes effectively read-only, and
attempts to change it will throw an exception. The specification of proper
UsageHints drives the system to make better decisions on how to process or
accelerate certain operations based on the anticipated usage pattern. Note
that those hints do not affect behavioral or visual results, but only affect
the overall performance of the panel and the elements within. It's advised to
always consider specifying the proper UsageHints, but keep in mind that some
UsageHints might be internally ignored under certain conditions (e.g. due to
hardware limitations on the target platform).  
[userData](UIElements.VisualElement-userData.html)|  This property can be used
to associate application-specific user data with this VisualElement.  
[viewDataKey](UIElements.VisualElement-viewDataKey.html)|  Used for view data
persistence, such as tree expanded states, scroll position, or zoom level.  
[visible](UIElements.VisualElement-visible.html)|  Indicates whether or not
this element should be rendered.  
[visualTreeAssetSource](UIElements.VisualElement-visualTreeAssetSource.html)|
Stores the asset reference, if the generated element is cloned from a
VisualTreeAsset.  
[worldBound](UIElements.VisualElement-worldBound.html)|  Returns a Rect
representing the Axis-aligned Bounding Box (AABB) after applying the world
transform.  
[worldTransform](UIElements.VisualElement-worldTransform.html)|  Returns a
matrix that cumulates the following operations (in order): -Local Scaling
-Local Rotation -Local Translation -Layout Translation -Parent worldTransform
(recursive definition - consider identity when there is no parent)  
  
### Public Methods

[SetValueWithoutNotify](UIElements.BaseField_1.SetValueWithoutNotify.html)|
Allow to set a value without being notified of the change, if any.  
---|---  
[HasBubbleUpHandlers](UIElements.CallbackEventHandler.HasBubbleUpHandlers.html)|
Return true if event handlers for the event propagation BubbleUp phase have
been attached to this object.  
[HasTrickleDownHandlers](UIElements.CallbackEventHandler.HasTrickleDownHandlers.html)|
Returns true if event handlers, for the event propagation TrickleDown phase,
are attached to this object.  
[RegisterCallback](UIElements.CallbackEventHandler.RegisterCallback.html)|
Adds an event handler to the instance. If the event handler has already been
registered for the same phase (either TrickleDown or BubbleUp) then this
method has no effect.  
[RegisterCallbackOnce](UIElements.CallbackEventHandler.RegisterCallbackOnce.html)|
Adds an event handler to the instance. If the event handler has already been
registered for the same phase (either TrickleDown or BubbleUp) then this
method has no effect. The event handler is automatically unregistered after it
has been invoked exactly once.  
[UnregisterCallback](UIElements.CallbackEventHandler.UnregisterCallback.html)|
Remove callback from the instance.  
[Blur](UIElements.Focusable.Blur.html)|  Tell the element to release the
focus.  
[Focus](UIElements.Focusable.Focus.html)|  Attempt to give the focus to this
element.  
[Add](UIElements.VisualElement.Add.html)|  Add an element to this element's
contentContainer  
[AddToClassList](UIElements.VisualElement.AddToClassList.html)|  Adds a class
to the class list of the element in order to assign styles from USS. Note the
class name is case-sensitive.  
[BringToFront](UIElements.VisualElement.BringToFront.html)|  Brings this
element to the end of its parent children list. The element will be visually
in front of any overlapping sibling elements.  
[Children](UIElements.VisualElement.Children.html)|  Returns the elements from
its contentContainer.  
[ClassListContains](UIElements.VisualElement.ClassListContains.html)|
Searches for a class in the class list of this element.  
[Clear](UIElements.VisualElement.Clear.html)|  Remove all child elements from
this element's contentContainer  
[ClearBinding](UIElements.VisualElement.ClearBinding.html)|  Removes a binding
from the element.  
[ClearBindings](UIElements.VisualElement.ClearBindings.html)|  Removes all
bindings from the element.  
[ClearClassList](UIElements.VisualElement.ClearClassList.html)|  Removes all
classes from the class list of this element. AddToClassList  
[Contains](UIElements.VisualElement.Contains.html)|  Checks if this element is
an ancestor of the specified child element.  
[ContainsPoint](UIElements.VisualElement.ContainsPoint.html)|  Checks if the
specified point intersects with this VisualElement's layout.  
[ElementAt](UIElements.VisualElement.ElementAt.html)|  Retrieves the child
element at a specific index.  
[EnableInClassList](UIElements.VisualElement.EnableInClassList.html)|  Enables
or disables the class with the given name.  
[FindAncestorUserData](UIElements.VisualElement.FindAncestorUserData.html)|
Searches up the hierarchy of this VisualElement and retrieves stored userData,
if any is found.  
[FindCommonAncestor](UIElements.VisualElement.FindCommonAncestor.html)|  Finds
the lowest common ancestor between two VisualElements inside the VisualTree
hierarchy.  
[GetBinding](UIElements.VisualElement.GetBinding.html)|  Gets the binding
instance for the provided targeted property.  
[GetBindingInfos](UIElements.VisualElement.GetBindingInfos.html)|  Gets
information on all the bindings of the current element.  
[GetClasses](UIElements.VisualElement.GetClasses.html)|  Retrieve the classes
for this element.  
[GetDataSourceContext](UIElements.VisualElement.GetDataSourceContext.html)|
Queries the dataSource and dataSourcePath of a binding object.  
[GetFirstAncestorOfType](UIElements.VisualElement.GetFirstAncestorOfType.html)|
Walks up the hierarchy, starting from this element's parent, and returns the
first VisualElement of this type  
[GetFirstOfType](UIElements.VisualElement.GetFirstOfType.html)|  Walks up the
hierarchy, starting from this element, and returns the first VisualElement of
this type  
[GetHierarchicalDataSourceContext](UIElements.VisualElement.GetHierarchicalDataSourceContext.html)|
Queries the dataSource and dataSourcePath inherited from the hierarchy.  
[HasBinding](UIElements.VisualElement.HasBinding.html)|  Allows to know if a
target property has a binding associated to it.  
[IndexOf](UIElements.VisualElement.IndexOf.html)|  Retrieves the child index
of the specified VisualElement.  
[Insert](UIElements.VisualElement.Insert.html)|  Insert an element into this
element's contentContainer  
[MarkDirtyRepaint](UIElements.VisualElement.MarkDirtyRepaint.html)|  Triggers
a repaint of the VisualElement on the next frame. This method is called
internally when a change occurs that requires a repaint, such as when
UIElements.BaseField_1.value is changed or the text in a Label. If you are
implementing a custom control, you can call this method to trigger a repaint
when a change occurs that requires a repaint such as when using
generateVisualContent to render a mesh and the mesh data has now changed.  
[PlaceBehind](UIElements.VisualElement.PlaceBehind.html)|  Places this element
right before the sibling element in their parent children list. If the element
and the sibling position overlap, the element will be visually behind of its
sibling.  
[PlaceInFront](UIElements.VisualElement.PlaceInFront.html)|  Places this
element right after the sibling element in their parent children list. If the
element and the sibling position overlap, the element will be visually in
front of its sibling.  
[Remove](UIElements.VisualElement.Remove.html)|  Removes this child from the
contentContainerhierarchy.  
[RemoveAt](UIElements.VisualElement.RemoveAt.html)|  Remove the child element
located at this position from this element's contentContainer  
[RemoveFromClassList](UIElements.VisualElement.RemoveFromClassList.html)|
Removes a class from the class list of the element.  
[RemoveFromHierarchy](UIElements.VisualElement.RemoveFromHierarchy.html)|
Removes this element from its parent hierarchy.  
[SendEvent](UIElements.VisualElement.SendEvent.html)|  Sends an event to the
event handler.  
[SendToBack](UIElements.VisualElement.SendToBack.html)|  Sends this element to
the beginning of its parent children list. The element will be visually behind
any overlapping sibling elements.  
[SetBinding](UIElements.VisualElement.SetBinding.html)|  Assigns a binding
between a target and a source.  
[SetEnabled](UIElements.VisualElement.SetEnabled.html)|  Changes the
VisualElement enabled state. A disabled VisualElement does not receive most
events.  
[Sort](UIElements.VisualElement.Sort.html)|  Reorders child elements from this
VisualElement contentContainer.  
[ToggleInClassList](UIElements.VisualElement.ToggleInClassList.html)|  Toggles
between adding and removing the given class name from the class list.  
[TryGetBinding](UIElements.VisualElement.TryGetBinding.html)|  Gets the
binding instance for the provided targeted property.  
[TryGetDataSourceContext](UIElements.VisualElement.TryGetDataSourceContext.html)|
Queries the dataSource and dataSourcePath of a binding object.  
[TryGetLastBindingToSourceResult](UIElements.VisualElement.TryGetLastBindingToSourceResult.html)|
Returns the last BindingResult of a binding object from the UI to the data
source.  
[TryGetLastBindingToUIResult](UIElements.VisualElement.TryGetLastBindingToUIResult.html)|
Returns the last BindingResult of a binding object from the data source to the
UI.  
  
### Protected Methods

[UpdateMixedValueContent](UIElements.BaseField_1.UpdateMixedValueContent.html)|
Update the field's visual content depending on showMixedValue.  
---|---  
[HandleEventBubbleUp](UIElements.CallbackEventHandler.HandleEventBubbleUp.html)|
Executes logic on this element during the BubbleUp phase, immediately before
this element's BubbleUp callbacks. Calling StopPropagation will prevent
further invocations of this method along the propagation path.  
[HandleEventTrickleDown](UIElements.CallbackEventHandler.HandleEventTrickleDown.html)|
Executes logic on this element during the TrickleDown phase, immediately after
this element's TrickleDown callbacks. Calling StopPropagation will prevent
further invocations of this method along the propagation path.  
[NotifyPropertyChanged](UIElements.CallbackEventHandler.NotifyPropertyChanged.html)|
Informs the data binding system that a property of a control has changed.  
  
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

