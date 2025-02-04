[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/UIE-IMGUI-migration.html)
  * [中文](/cn/current/Manual/UIE-IMGUI-migration.html)
  * [日本語](/ja/current/Manual/UIE-IMGUI-migration.html)
  * [한국어](/kr/current/Manual/UIE-IMGUI-migration.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/UIE-IMGUI-migration.html)
  * [中文](/cn/current/Manual/UIE-IMGUI-migration.html)
  * [日本語](/ja/current/Manual/UIE-IMGUI-migration.html)
  * [한국어](/kr/current/Manual/UIE-IMGUI-migration.html)

  * [Working in Unity](working-in-unity.html)
  * [User interface (UI)](UIToolkits.html)
  * [UI Toolkit](UIElements.html)
  * [Migration guides](UIE-migration-guides.html)
  * Migrate from Immediate Mode GUI (IMGUI) to UI Toolkit

[](UIE-Transitioning-From-UGUI.html)

Migrate from Unity UI (uGUI) to UI Toolkit

[](com.unity.ugui.html)

Unity UI

# Migrate from Immediate Mode GUI (IMGUI) to UI Toolkit

This guide is for developers experienced with [Immediate Mode GUI
(IMGUI)](GUIScriptingGuide.html) to migrate to **UI**(User Interface) Allows a
user to interact with your application. Unity currently supports three UI
systems. [More info](UI-system-compare.html)  
See in [Glossary](Glossary.html#UI) Toolkit. This guide focuses on the Editor
UI, but its information can also apply to the runtime UI as well.

## Key differences

### Code-driven versus UI-driven

IMGUI is code-driven by calls to the `OnGUI` function in a C# script that
implements it. UI Toolkit provides more options for Editor UI creation. With
UI Toolkit, you define the behaviors in C# **scripts** A piece of code that
allows you to create your own Components, trigger game events, modify
Component properties over time and respond to user input in any way you like.
[More info](creating-scripts.html)  
See in [Glossary](Glossary.html#Scripts). However, when defining UI elements
and styles, in addition to C#, you can visually define UI controls in [UI
Builder](UIBuilder.html) or write in [an XML-like text file (called
UXML)](UIE-UXML.html) directly. For more information, refer to [Get started
with UI Toolkit](UIE-simple-ui-toolkit-workflow.html).

### Immediate versus retained mode

With IMGUI, you describe the UI tree when the UI is repainted within the
[`OnGUI()`](../ScriptReference/EditorWindow.OnGUI.html) function. You must
call this function when an event enters the UI or when you repaint the UI.
There is no persistent information pertaining to the UI tree between different
events. Whereas, you create **visual elements** A node of a visual tree that
instantiates or derives from the C#
[`VisualElement`](../ScriptReference/UIElements.VisualElement.html) class. You
can style the look, define the behaviour, and display it on screen as part of
the UI. [More info](UIE-VisualTree.html)  
See in [Glossary](Glossary.html#Visualelement) with UI Toolkit in a tree
structure called [Visual Tree](UIE-VisualTree.html)An object graph, made of
lightweight nodes, that holds all the elements in a window or panel. It
defines every UI you build with the UI Toolkit.  
See in [Glossary](Glossary.html#Visualtree). Information in the Visual Trees
is retained persistently.

### Constant versus state changes

IMGUI is based on the `OnGUI`()`function that runs at least once every frame.
You define the look and the behaviors of the UI for every possible frame. The
body of`OnGUI()` might contain many conditions and different states.

UI Toolkit operates in an event-driven system. You define the look of the UI
in its default state and define the behaviors of the UI in response to events.
Any changes you make in UI Toolkit cause persistent changes to the state of
your UI.

For example, the declaration of a button in IMGUI looks like the following:

    
    
    if (GUILayout.Button("Click me!"))
    {
        //Code runs here in frames where the user clicks the button.
    
        //Code makes changes to the UI for frames where the user has just clicked the button.
    }
    else
    {
        //Code specifies what happens in all other frames.
    }
    

The example above looks like the following in UI Toolkit:

    
    
    UIDocument document = GetComponent<UIDocument>();
    
    //Create button.
    Button button = new Button();
    button.text = "Click me!";
    
    //Set up event handler.
    button.RegisterCallback<ClickEvent>((ClickEvent evt) =>
    {
        //Code runs here after button receives ClickEvent.
    });
    
    //Add button to UI.
    document.rootVisualElement.Add(button);
    

For a completed example of how to create a custom Editor window with UI
Toolkit, refer to [Get started with UI Toolkit](UIE-simple-ui-toolkit-
workflow.html).

## IMGUI support

Use the `IMGUIContainer` to place IMGUI code inside of a `VisualElement`.
Everything you can do inside of `OnGUI()` is supported.

You can arrange multiple `IMGUIContainer`s and lay them out by mixing
`GUILayout` and UI Toolkit layouts. Note that it’s not possible to add
`VisualElement` instances inside of an `IMGUIContainer`.

![IMGUIContainer example](../uploads/Main/UIElementsIMGUI.png)
`IMGUIContainer` example

## From IMGUI to UI Toolkit conversion

The following table lists the equivalent functions between IMGUI and UI
Toolkit:

**Action** | **IMGUI** | **UI Toolkit**  
---|---|---  
Create an [Editor Window](editor-EditorWindows.html) | [`EditorWindow.OnGUI()`](../ScriptReference/EditorWindow.OnGUI.html) | [`EditorWindow.CreateGUI()`](../ScriptReference/EditorWindow.CreateGUI.html)  
Create a [Property Drawer](editor-PropertyDrawers.html)A Unity feature that
allows you to customize the look of certain controls in the Inspector window
by using attributes on your scripts, or by controlling how a specific
Serializable class should look [More info](editor-PropertyDrawers.html)  
See in [Glossary](Glossary.html#PropertyDrawer) or a Property Attribute | [`PropertyDrawer.OnGUI()`](../ScriptReference/PropertyDrawer.OnGUI.html) | [`PropertyDrawer.CreatePropertyGUI()`](../ScriptReference/PropertyDrawer.CreatePropertyGUI.html)  
Create a custom Editor for the ****Inspector** A Unity window that displays
information about the currently selected GameObject, asset or project
settings, allowing you to inspect and edit the values. [More
info](UsingTheInspector.html)  
See in [Glossary](Glossary.html#Inspector)** | [`Editor.OnInspectorGUI()`](../ScriptReference/Editor.OnInspectorGUI.html) | [`Editor.CreateInspectorGUI()`](../ScriptReference/Editor.CreateInspectorGUI.html)  
  
The following table lists the equivalent methods, classes, and attributes
between IMGUI and UI Toolkit:

**IMGUI** | **IMGUI namespaces** | **UI Toolkit**  
---|---|---  
[`AddCursorRect()`](../ScriptReference/EditorGUIUtility.AddCursorRect.html) | EditorGUIUtility | Set [`VisualElement.style.cursor`](../ScriptReference/UIElements.IStyle-cursor.html), or set a visual element’s cursor texture in the UI Builder or USS. For more detailed interactivity, use C# events.  
[`AreaScope`](../ScriptReference/GUILayout.AreaScope.html) | GUILayout | Scopes are generally not needed in UI Toolkit. See `BeginArea()`.  
[`BeginArea()`](../ScriptReference/GUILayout.BeginArea.html) | GUILayout | To define the area itself, create a visual element and set [`style.position`](../ScriptReference/UIElements.IStyle-position.html) to [`Position.Absolute`](../ScriptReference/UIElements.Position.Absolute.html). To create children for the area, create child visual elements under it.  
[`BeginBuildTargetSelectionGrouping()`](../ScriptReference/EditorGUILayout.BeginBuildTargetSelectionGrouping.html) | EditorGUILayout | No equivalent.  
[`BeginChangeCheck()`](../ScriptReference/EditorGUI.BeginChangeCheck.html) | EditorGUI | Register callbacks on each element in the change check range. If using a [`PropertyField`](../ScriptReference/UIElements.PropertyField.html) as a stand-in for a serialized field in a custom Inspector, use [`PropertyField.RegisterCallback<SerializedPropertyChangeEvent>()`](../ScriptReference/UIElements.CallbackEventHandler.RegisterCallback.html) or [`PropertyField.RegisterValueChangeCallback()`](../ScriptReference/UIElements.PropertyField.RegisterValueChangeCallback.html). In all other cases, use [`VisualElement.RegisterCallback<ChangeEvent<T>>()`](../ScriptReference/UIElements.CallbackEventHandler.RegisterCallback.html) or [`VisualElement.RegisterValueChangedCallback<T>()`](../ScriptReference/UIElements.INotifyValueChangedExtensions.RegisterValueChangedCallback.html).  
[`BeginDisabledGroup()`](../ScriptReference/EditorGUI.BeginDisabledGroup.html) | EditorGUI | [`VisualElement.SetEnabled(false)`](../ScriptReference/UIElements.VisualElement.SetEnabled.html)  
[`BeginFoldoutHeaderGroup()`](../ScriptReference/EditorGUI.BeginFoldoutHeaderGroup.html) | EditorGUI, EditorGUILayout | See `Foldout()`.  
[`BeginGroup()`](../ScriptReference/GUI.BeginGroup.html) | GUI | See `BeginArea()`.  
[`BeginHorizontal()`](../ScriptReference/EditorGUILayout.BeginHorizontal.html) | EditorGUILayout, GUILayout | See `BeginArea()`.  
[`BeginProperty()`](../ScriptReference/EditorGUI.BeginProperty.html) | EditorGUI | If you use `BeginProperty()`/`EndProperty()` to bind a simple control to a serialized property, you can do that in UI Toolkit by calling [`BindProperty()`](../ScriptReference/UIElements.BindingExtensions.BindProperty.html), by setting [`bindingPath`](../ScriptReference/UIElements.BindableElement-bindingPath.html), or by setting the `binding-path` UXML attribute. If you use `BeginProperty()`/`EndProperty()` to make a single property out of complex custom UI, that is not supported well in UI Toolkit.  
[`BeginScrollView()`](../ScriptReference/GUI.BeginScrollView.html) | EditorGUILayout, GUI, GUILayout | [`UnityEngine.UIElements.ScrollView`](../ScriptReference/UIElements.ScrollView.html)  
[`BeginToggleGroup()`](../ScriptReference/EditorGUILayout.BeginToggleGroup.html) | EditorGUILayout | No equivalent.  
[`BeginVertical()`](../ScriptReference/EditorGUILayout.BeginVertical.html) | EditorGUILayout, GUILayout | See `BeginArea()`.  
[`BoundsField()`](../ScriptReference/EditorGUI.BoundsField.html) | EditorGUI, EditorGUILayout | [`BoundsField`](../ScriptReference/UIElements.BoundsField.html)  
[`BoundsIntField()`](../ScriptReference/EditorGUI.BoundsIntField.html) | EditorGUI, EditorGUILayout | [`BoundsIntField`](../ScriptReference/UIElements.BoundsIntField.html)  
[`Box()`](../ScriptReference/GUI.Box.html) | GUI, GUILayout | [`Box`](../ScriptReference/UIElements.Box.html)  
[`BringWindowToBack()`](../ScriptReference/GUI.BringWindowToBack.html) | GUI | See `Window()`.  
[`BringWindowToFront()`](../ScriptReference/GUI.BringWindowToFront.html) | GUI | See `Window()`.  
[`Button()`](../ScriptReference/GUI.Button.html) | GUI, GUILayout | [`Button`](../ScriptReference/UIElements.Button.html)  
[`CanCacheInspectorGUI()`](../ScriptReference/EditorGUI.CanCacheInspectorGUI.html) | EditorGUI | Not needed in retained mode.  
[`ChangeCheckScope`](../ScriptReference/EditorGUI.ChangeCheckScope.html) | EditorGUI | Scopes are generally not needed in UI Toolkit. See `BeginChangeCheck()`.  
[`ColorField()`](../ScriptReference/EditorGUI.ColorField.html) | EditorGUI, EditorGUILayout | [`ColorField`](../ScriptReference/UIElements.ColorField.html)  
[`CommandEvent()`](../ScriptReference/EditorGUIUtility.CommandEvent.html) | EditorGUIUtility | Generally not needed in retained mode. Use C# callbacks to handle events.  
[`CurveField()`](../ScriptReference/EditorGUI.CurveField.html) | EditorGUI, EditorGUILayout | [`CurveField`](../ScriptReference/UIElements.CurveField.html)  
[`DelayedDoubleField()`](../ScriptReference/EditorGUI.DelayedDoubleField.html) | EditorGUI, EditorGUILayout |  [`DoubleField`](../ScriptReference/UIElements.DoubleField.html) with [`isDelayed`](../ScriptReference/UIElements.TextInputBaseField_1-isDelayed.html) set to true.  
[`DelayedFloatField()`](../ScriptReference/EditorGUI.DelayedFloatField.html) | EditorGUI, EditorGUILayout |  [`FloatField`](../ScriptReference/UIElements.FloatField.html) with [`isDelayed`](../ScriptReference/UIElements.TextInputBaseField_1-isDelayed.html) set to true.  
[`DelayedIntField()`](../ScriptReference/EditorGUI.DelayedIntField.html) | EditorGUI, EditorGUILayout |  [`IntegerField`](../ScriptReference/UIElements.IntegerField.html) with [`isDelayed`](../ScriptReference/UIElements.TextInputBaseField_1-isDelayed.html) set to true.  
[`DelayedTextField()`](../ScriptReference/EditorGUI.DelayedTextField.html) | EditorGUI, EditorGUILayout |  [`TextField`](../ScriptReference/UIElements.TextField.html) with [`isDelayed`](../ScriptReference/UIElements.TextInputBaseField_1-isDelayed.html) set to true.  
[`DisabledScope`](../ScriptReference/EditorGUI.DisabledScope.html) | EditorGUI | Scopes are generally not needed in UI Toolkit. See `BeginDisabledGroup()`.  
[`DoubleField()`](../ScriptReference/EditorGUI.DoubleField.html) | EditorGUI, EditorGUILayout | [`DoubleField`](../ScriptReference/UIElements.DoubleField.html)  
[`DragWindow()`](../ScriptReference/GUI.DragWindow.html) | GUI | See `Window()`.  
[`DrawPreviewTexture()`](../ScriptReference/EditorGUI.DrawPreviewTexture.html) | EditorGUI | No equivalent.  
[`DrawRect()`](../ScriptReference/EditorGUI.DrawRect.html) | EditorGUI | Use [`VisualElement`](../ScriptReference/UIElements.VisualElement.html). Set [`style.position`](../ScriptReference/UIElements.IStyle-position.html) to [`Absolute`](../ScriptReference/UIElements.Position.Absolute.html). Set [`style.top`](../ScriptReference/UIElements.IStyle-top.html) and [`style.left`](../ScriptReference/UIElements.IStyle-left.html) to define the position. Set [`style.width`](../ScriptReference/UIElements.IStyle-width.html) and [`style.height`](../ScriptReference/UIElements.IStyle-height.html) to define the size. Set [`style.backgroundColor`](../ScriptReference/UIElements.IStyle-backgroundColor.html) to set the color.  
[`DrawTexture()`](../ScriptReference/GUI.DrawTexture.html) | GUI |  [`Image`](../ScriptReference/UIElements.Image.html). Set [`tintColor`](../ScriptReference/UIElements.Image-tintColor.html) in place of `color`. There is no equivalent for a false `alphaBlend`. There are no equivalents for `borderWidth`, `borderWidths`, `borderRadius`, or `borderRadiuses`.  
[`DrawTextureAlpha()`](../ScriptReference/EditorGUI.DrawTextureAlpha.html) | EditorGUI | No equivalent.  
[`DrawTextureWithTexCoords()`](../ScriptReference/GUI.DrawTextureWithTexCoords.html) | GUI |  [`Image`](../ScriptReference/UIElements.Image.html). Set [`uv`](../ScriptReference/UIElements.Image-uv.html) in place of `texCoords`. There is no equivalent for a false `alphaBlend`.  
[`DropdownButton()`](../ScriptReference/EditorGUI.DropdownButton.html) | EditorGUI, EditorGUILayout | No exact equivalent. Use fully-fledged [`DropdownField`](../ScriptReference/UIElements.DropdownField.html)s instead of just a `DropdownButton()`.  
[`DropShadowLabel()`](../ScriptReference/EditorGUI.DropShadowLabel.html) | EditorGUI |  [`Label`](../ScriptReference/UIElements.Label.html) with shadow values set in [`style.textShadow`](../ScriptReference/UIElements.IStyle-textShadow.html).  
[`EditorToolbar()`](../ScriptReference/EditorGUILayout.EditorToolbar.html) | EditorGUILayout | Create a [`Toolbar`](../ScriptReference/UIElements.Toolbar.html) with one [`ToolbarButton`](../ScriptReference/UIElements.ToolbarButton.html) for each tool. For each `ToolbarButton`, register a callback when clicked to call either [`ToolManager.SetActiveTool()`](../ScriptReference/EditorTools.ToolManager.SetActiveTool.html) or [`ToolManager.RestorePreviousTool()`](../ScriptReference/EditorTools.ToolManager.RestorePreviousTool.html) to make that button activate the tool or deactivate it, respectively.  
[`EndArea()`](../ScriptReference/GUILayout.EndArea.html) | GUILayout | See `BeginArea()`.  
[`EndBuildTargetSelectionGrouping()`](../ScriptReference/EditorGUILayout.EndBuildTargetSelectionGrouping.html) | EditorGUILayout | See `BeginBuildTargetSelectionGrouping()`.  
[`EndChangeCheck()`](../ScriptReference/EditorGUI.EndChangeCheck.html) | EditorGUI | See `BeginChangeCheck()`.  
[`EndDisabledGroup()`](../ScriptReference/EditorGUI.EndDisabledGroup.html) | EditorGUI | See `BeginDisabledGroup()`.  
[`EndFoldoutHeaderGroup()`](../ScriptReference/EditorGUI.EndFoldoutHeaderGroup.html) | EditorGUI, EditorGUILayout | See `Foldout()`.  
[`EndGroup()`](../ScriptReference/GUI.EndGroup.html) | GUI | See `BeginArea()`.  
[`EndHorizontal()`](../ScriptReference/EditorGUILayout.EndHorizontal.html) | EditorGUILayout, GUILayout | See `BeginArea()`.  
[`EndProperty()`](../ScriptReference/EditorGUI.EndProperty.html) | EditorGUI | See `BeginProperty()`.  
[`EndScrollView()`](../ScriptReference/GUI.EndScrollView.html) | EditorGUILayout, GUI, GUILayout | See `BeginScrollView()`.  
[`EndToggleGroup()`](../ScriptReference/EditorGUILayout.EndToggleGroup.html) | EditorGUILayout | See `BeginToggleGroup()`.  
[`EndVertical()`](../ScriptReference/EditorGUILayout.EndVertical.html) | EditorGUILayout, GUILayout | See `BeginArea()`.  
[`EnumFlagsField()`](../ScriptReference/EditorGUI.EnumFlagsField.html) | EditorGUI, EditorGUILayout | [`EnumFlagsField`](../ScriptReference/UIElements.EnumFlagsField.html)  
[`EnumPopup()`](../ScriptReference/EditorGUI.EnumPopup.html) | EditorGUI, EditorGUILayout | [`EnumField`](../ScriptReference/UIElements.EnumField.html)  
[`ExpandHeight()`](../ScriptReference/GUILayout.ExpandHeight.html) | GUILayout | No equivalent.  
[`ExpandWidth()`](../ScriptReference/GUILayout.ExpandWidth.html) | GUILayout | No equivalent.  
[`FlexibleSpace()`](../ScriptReference/GUILayout.FlexibleSpace.html) | GUILayout | See `Space()`.  
[`FloatField()`](../ScriptReference/EditorGUI.FloatField.html) | EditorGUI, EditorGUILayout | [`FloatField`](../ScriptReference/UIElements.FloatField.html)  
[`FocusControl()`](../ScriptReference/GUI.FocusControl.html) | GUI | [`VisualElement.Focus()`](../ScriptReference/UIElements.Focusable.Focus.html)  
[`FocusTextInControl()`](../ScriptReference/EditorGUI.FocusTextInControl.html) | EditorGUI | [`TextField.Focus()`](../ScriptReference/UIElements.Focusable.Focus.html)  
[`FocusWindow()`](../ScriptReference/GUI.FocusWindow.html) | GUI | See `Window()`.  
[`Foldout()`](../ScriptReference/EditorGUI.Foldout.html) | EditorGUI, EditorGUILayout | [`Foldout`](../ScriptReference/UIElements.Foldout.html)  
[`GetControlRect()`](../ScriptReference/EditorGUILayout.GetControlRect.html) | EditorGUILayout | Only needed to convert from EditorGUILayout to EditorGUI. Not needed in UI Toolkit.  
[`GetNameOfFocusedControl()`](../ScriptReference/GUI.GetNameOfFocusedControl.html) | GUI | [`VisualElement.focusController.focusedElement`](../ScriptReference/UIElements.FocusController-focusedElement.html)  
[`GetPropertyHeight()`](../ScriptReference/EditorGUI.GetPropertyHeight.html) | EditorGUI | [`PropertyField.layout.height`](../ScriptReference/Rect-height.html)  
[`GradientField()`](../ScriptReference/EditorGUI.GradientField.html) | EditorGUI, EditorGUILayout | [`GradientField`](../ScriptReference/UIElements.GradientField.html)  
[`GroupScope`](../ScriptReference/GUI.GroupScope.html) | GUI | Scopes are generally not needed in UI Toolkit. See `BeginArea()`.  
[`Height()`](../ScriptReference/GUILayout.Height.html) | GUILayout | [`VisualElement.style.height`](../ScriptReference/UIElements.IStyle-height.html)  
[`HelpBox()`](../ScriptReference/EditorGUI.HelpBox.html) | EditorGUI, EditorGUILayout | [`HelpBox`](../ScriptReference/UIElements.HelpBox.html)  
[`HorizontalScope`](../ScriptReference/EditorGUILayout.HorizontalScope.html) | EditorGUILayout, GUILayout | Scopes are generally not needed in UI Toolkit. See `BeginArea()`.  
[`HorizontalScrollbar()`](../ScriptReference/GUI.HorizontalScrollbar.html) | GUI, GUILayout |  [`Scroller`](../ScriptReference/UIElements.Scroller.html) with [`direction`](../ScriptReference/UIElements.Scroller-direction.html) set to [`Horizontal`](../ScriptReference/UIElements.SliderDirection.Horizontal.html).  
[`HorizontalSlider()`](../ScriptReference/GUI.HorizontalSlider.html) | GUI, GUILayout |  [`Slider`](../ScriptReference/UIElements.Slider.html) with [`direction`](../ScriptReference/UIElements.BaseSlider_1-direction.html) set to [`Horizontal`](../ScriptReference/UIElements.SliderDirection.Horizontal.html)  
[`InspectorTitlebar()`](../ScriptReference/EditorGUI.InspectorTitlebar.html) | EditorGUI, EditorGUILayout | No equivalent.  
[`IntField()`](../ScriptReference/EditorGUI.IntField.html) | EditorGUI, EditorGUILayout | [`IntegerField`](../ScriptReference/UIElements.IntegerField.html)  
[`IntPopup()`](../ScriptReference/EditorGUI.IntPopup.html) | EditorGUI, EditorGUILayout | No equivalent.  
[`IntSlider()`](../ScriptReference/EditorGUI.IntSlider.html) | EditorGUI, EditorGUILayout | [`SliderInt`](../ScriptReference/UIElements.SliderInt.html)  
[`Label()`](../ScriptReference/GUI.Label.html) | GUI, GUILayout | [`Label`](../ScriptReference/UIElements.Label.html)  
[`LabelField()`](../ScriptReference/EditorGUI.LabelField.html) | EditorGUI, EditorGUILayout |  [`TextField`](../ScriptReference/UIElements.TextField.html) with [`isReadOnly`](../ScriptReference/UIElements.TextInputBaseField_1-isReadOnly.html) set to true.  
[`LayerField()`](../ScriptReference/EditorGUI.LayerField.html) | EditorGUI, EditorGUILayout | [`LayerField`](../ScriptReference/EditorGUI.LayerField.html)  
[`LinkButton()`](../ScriptReference/EditorGUI.LinkButton.html) | EditorGUI, EditorGUILayout | No equivalent.  
[`Load()`](../ScriptReference/EditorGUIUtility.Load.html) | EditorGUIUtility | If using C#, you can use this function as is and assign its return value to the `VisualElement.style` property you want. If using USS, use function `resource()` with the same argument you would give to `Load()`.  
[`LongField()`](../ScriptReference/EditorGUI.LongField.html) | EditorGUI, EditorGUILayout | [`LongField`](../ScriptReference/UIElements.LongField.html)  
[`MaskField()`](../ScriptReference/EditorGUI.MaskField.html) | EditorGUI, EditorGUILayout | [`MaskField`](../ScriptReference/UIElements.MaskField.html)  
[`MaxHeight()`](../ScriptReference/GUILayout.MaxHeight.html) | GUILayout | [`VisualElement.style.maxHeight`](../ScriptReference/UIElements.IStyle-maxHeight.html)  
[`MaxWidth()`](../ScriptReference/GUILayout.MaxWidth.html) | GUILayout | [`VisualElement.style.maxWidth`](../ScriptReference/UIElements.IStyle-maxWidth.html)  
[`MinHeight()`](../ScriptReference/GUILayout.MinHeight.html) | GUILayout | [`VisualElement.style.minHeight`](../ScriptReference/UIElements.IStyle-minHeight.html)  
[`MinMaxSlider()`](../ScriptReference/EditorGUI.MinMaxSlider.html) | EditorGUI, EditorGUILayout | [`MinMaxSlider`](../ScriptReference/UIElements.MinMaxSlider.html)  
[`MinWidth()`](../ScriptReference/GUILayout.MinWidth.html) | GUILayout | [`VisualElement.style.minWidth`](../ScriptReference/UIElements.IStyle-minWidth.html)  
[`ModalWindow()`](../ScriptReference/GUI.ModalWindow.html) | GUI | See `Window()`.  
[`[NonReorderable]` attribute](../ScriptReference/NonReorderableAttribute.html) |  | Ensure that [`ListView.reorderable`](../ScriptReference/UIElements.BaseVerticalCollectionView-reorderable.html) is false.  
[`ObjectField()`](../ScriptReference/EditorGUI.ObjectField.html) | EditorGUI, EditorGUILayout | [`ObjectField`](../ScriptReference/UIElements.ObjectField.html)  
[`PasswordField()`](../ScriptReference/EditorGUI.PasswordField.html) | EditorGUI, EditorGUILayout, GUI, GUILayout |  [`TextField`](../ScriptReference/UIElements.TextField.html) with [`isPasswordField`](../ScriptReference/UIElements.TextInputBaseField_1-isPasswordField.html) set to true  
[`PixelsToPoints()`](../ScriptReference/EditorGUIUtility.PixelsToPoints.html) | EditorGUIUtility | Valid for use with UI Toolkit.  
[`PointsToPixels()`](../ScriptReference/EditorGUIUtility.PointsToPixels.html) | EditorGUIUtility | Valid for use with UI Toolkit.  
[`Popup()`](../ScriptReference/EditorGUI.Popup.html) | EditorGUI, EditorGUILayout | [`PopupField<T0>`](../ScriptReference/UIElements.PopupField_1.html)  
[`ProgressBar()`](../ScriptReference/EditorGUI.ProgressBar.html) | EditorGUI | [`ProgressBar`](../ScriptReference/UIElements.ProgressBar.html)  
[`PropertyField()`](../ScriptReference/EditorGUI.PropertyField.html) | EditorGUI, EditorGUILayout | [`PropertyField`](../ScriptReference/UIElements.PropertyField.html)  
[`PropertyScope`](../ScriptReference/EditorGUI.PropertyScope.html) | EditorGUI | Scopes are generally not needed in UI Toolkit. See `BeginProperty()`.  
[`RectField()`](../ScriptReference/EditorGUI.RectField.html) | EditorGUI, EditorGUILayout | [`RectField`](../ScriptReference/UIElements.RectField.html)  
[`RectIntField()`](../ScriptReference/EditorGUI.RectIntField.html) | EditorGUI, EditorGUILayout | [`RectIntField`](../ScriptReference/UIElements.RectIntField.html)  
[`RepeatButton()`](../ScriptReference/GUI.RepeatButton.html) | GUI, GUILayout | [`RepeatButton`](../ScriptReference/UIElements.RepeatButton.html)  
[`ScrollTo()`](../ScriptReference/GUI.ScrollTo.html) | GUI |  [`ScrollView.ScrollTo()`](../ScriptReference/UIElements.ScrollView.ScrollTo.html) or [`ScrollView.scrollOffset`](../ScriptReference/UIElements.ScrollView-scrollOffset.html)  
[`ScrollViewScope`](../ScriptReference/EditorGUILayout.ScrollViewScope.html) | EditorGUILayout, GUI, GUILayout | Scopes are generally not needed in UI Toolkit. See `BeginScrollView()`.  
[`SelectableLabel()`](../ScriptReference/EditorGUI.SelectableLabel.html) | EditorGUI, EditorGUILayout |  [`Label`](../ScriptReference/UIElements.Label.html) with [`isSelectable`](../ScriptReference/UIElements.ITextSelection-isSelectable.html) and [`focusable`](../ScriptReference/UIElements.Focusable-focusable.html) set to true.  
[`SelectionGrid()`](../ScriptReference/GUI.SelectionGrid.html) | GUI, GUILayout | [`RadioButton`](../ScriptReference/UIElements.RadioButton.html)  
[`SetNextControlName()`](../ScriptReference/GUI.SetNextControlName.html) | GUI | [`VisualElement.name`](../ScriptReference/UIElements.VisualElement-name.html)  
[`singleLineHeight`](../ScriptReference/EditorGUIUtility-singleLineHeight.html) | EditorGUIUtility | Use USS variable `--unity-metrics-single_line-height`.  
[`Slider()`](../ScriptReference/EditorGUI.Slider.html) | EditorGUI, EditorGUILayout | [`Slider`](../ScriptReference/UIElements.Slider.html)  
[`Space()`](../ScriptReference/EditorGUILayout.Space.html) | EditorGUILayout, GUILayout | Use `flex` properties to configure spacing between visual elements.  
[`TagField()`](../ScriptReference/EditorGUI.TagField.html) | EditorGUI, EditorGUILayout | [`TagField`](../ScriptReference/UIElements.TagField.html)  
[`TextArea()`](../ScriptReference/EditorGUI.TextArea.html) | EditorGUI, EditorGUILayout, GUI, GUILayout |  [`TextField`](../ScriptReference/UIElements.TextField.html) with [`multiline`](../ScriptReference/UIElements.TextField-multiline.html) set to true, [`style.whiteSpace`](../ScriptReference/UIElements.IStyle-whiteSpace.html) set to [`Normal`](../ScriptReference/UIElements.WhiteSpace.Normal.html), and [`ScrollView.verticalScrollerVisibility`](../ScriptReference/UIElements.ScrollView-verticalScrollerVisibility.html) set to [`Auto`](../ScriptReference/UIElements.ScrollerVisibility.Auto.html).  
[`TextField()`](../ScriptReference/EditorGUI.TextField.html) | EditorGUI, EditorGUILayout, GUI, GUILayout |  [`TextField`](../ScriptReference/UIElements.TextField.html) with [`multiline`](../ScriptReference/UIElements.TextField-multiline.html) set to true and [`style.whiteSpace`](../ScriptReference/UIElements.IStyle-whiteSpace.html) set to [`NoWrap`](../ScriptReference/UIElements.WhiteSpace.NoWrap.html).  
[`Toggle()`](../ScriptReference/EditorGUI.Toggle.html) | EditorGUI, EditorGUILayout, GUI, GUILayout | [`Toggle`](../ScriptReference/UIElements.Toggle.html)  
[`ToggleGroupScope`](../ScriptReference/EditorGUILayout.ToggleGroupScope.html) | EditorGUILayout | Scopes are generally not needed in UI Toolkit. See `BeginToggleGroup()`.  
[`ToggleLeft()`](../ScriptReference/EditorGUI.ToggleLeft.html) | EditorGUI, EditorGUILayout |  [`Toggle`](../ScriptReference/UIElements.Toggle.html), but instead of setting [`label`](../ScriptReference/UIElements.BaseField_1-label.html), set [`text`](../ScriptReference/UIElements.BaseBoolField-text.html).  
[`Toolbar()`](../ScriptReference/GUI.Toolbar.html) | GUI, GUILayout | No equivalent.  
[`UnfocusWindow()`](../ScriptReference/GUI.UnfocusWindow.html) | GUI | See `Window()`.  
[`Vector2Field()`](../ScriptReference/EditorGUI.Vector2Field.html) | EditorGUI, EditorGUILayout | [`Vector2Field`](../ScriptReference/UIElements.Vector2Field.html)  
[`Vector2IntField()`](../ScriptReference/EditorGUI.Vector2IntField.html) | EditorGUI, EditorGUILayout | [`Vector2IntField`](../ScriptReference/UIElements.Vector2IntField.html)  
[`Vector3Field()`](../ScriptReference/EditorGUI.Vector3Field.html) | EditorGUI, EditorGUILayout | [`Vector3Field`](../ScriptReference/UIElements.Vector3Field.html)  
[`Vector3IntField()`](../ScriptReference/EditorGUI.Vector3IntField.html) | EditorGUI, EditorGUILayout | [`Vector3IntField`](../ScriptReference/UIElements.Vector3IntField.html)  
[`Vector4Field()`](../ScriptReference/EditorGUI.Vector4Field.html) | EditorGUI, EditorGUILayout | [`Vector4Field`](../ScriptReference/UIElements.Vector4Field.html)  
[`VerticalScope`](../ScriptReference/EditorGUILayout.VerticalScope.html) | EditorGUILayout, GUILayout | Scopes are generally not needed in UI Toolkit. See `BeginArea()`.  
[`VerticalScrollbar()`](../ScriptReference/GUI.VerticalScrollbar.html) | GUI, GUILayout |  [`Scroller`](../ScriptReference/UIElements.Scroller.html) with [`direction`](../ScriptReference/UIElements.Scroller-direction.html) set to [`Vertical`](../ScriptReference/UIElements.SliderDirection.Vertical.html).  
[`VerticalSlider()`](../ScriptReference/GUI.VerticalSlider.html) | GUI, GUILayout |  [`Slider`](../ScriptReference/UIElements.Slider.html) with [`direction`](../ScriptReference/UIElements.BaseSlider_1-direction.html) set to [`Vertical`](../ScriptReference/UIElements.SliderDirection.Vertical.html).  
[`Width()`](../ScriptReference/GUILayout.Width.html) | GUILayout | [`VisualElement.style.width`](../ScriptReference/UIElements.IStyle-width.html)  
[`Window()`](../ScriptReference/GUI.Window.html) | GUI, GUILayout | No equivalent.  
  
## Additional resources

  * [Get started with UI Toolkit](UIE-simple-ui-toolkit-workflow.html)
  * [Unity style sheets (USS)](UIE-USS.html)
  * [Examples](UIE-examples.html)
  * [IMGUI events](UIE-IMGUI-Events.html)

[](UIE-Transitioning-From-UGUI.html)

Migrate from Unity UI (uGUI) to UI Toolkit

[](com.unity.ugui.html)

Unity UI

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

