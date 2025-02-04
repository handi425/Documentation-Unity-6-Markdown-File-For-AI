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

# ToolbarOverlay

class in UnityEditor.Overlays

/

Inherits from:[Overlays.Overlay](Overlays.Overlay.html)

Leave feedback

  

Implements interfaces:[ICreateToolbar](Overlays.ICreateToolbar.html)

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

[ToolbarOverlay](Overlays.ToolbarOverlay.html) is an implementation of
[Overlay](Overlays.Overlay.html) that provides a base for Overlays that can be
placed in horizontal or vertical toolbars.

The constructor for [ToolbarOverlay](Overlays.ToolbarOverlay.html) accepts a
list of IDs corresponding to UnityEditor.Toolbars.EditorToolbarElement::id.  
  
Toolbars are composed of collections of
UnityEditor.Toolbars.EditorToolbarElement. In this way it is very simple to
reuse elements to create customized toolbars.  
  
Toolbar overlays require specific styling, so in most cases it is preferable
to inherit one of the predefined EditorToolbar types when creating Visual
Elements. If custom UI is required, it is valid to inherit any
UnityEngine.UIElements.VisualElement type and provide styling yourself.

    
    
    using [UnityEditor](UnityEditor.html);
    using UnityEditor.Overlays;
    using UnityEditor.Toolbars;
    using UnityEngine;
    
    // [EditorToolbarElement(Identifier, EditorWindowType)] is used to register toolbar elements for use in [ToolbarOverlay](Overlays.ToolbarOverlay.html)
    // implementations.
    [EditorToolbarElement(id, typeof([SceneView](SceneView.html)))]
    class CreateCubes : [EditorToolbarButton](Toolbars.EditorToolbarButton.html), [IAccessContainerWindow](Toolbars.IAccessContainerWindow.html)
    {
        // This ID is used to populate toolbar elements.
        public const string id = "ExampleToolbar/[Button](UIElements.Button.html)";
    
        // [IAccessContainerWindow](Toolbars.IAccessContainerWindow.html) provides a way for toolbar elements to access the `[EditorWindow](EditorWindow.html)` in which they exist.
        // Here we use `containerWindow` to focus the camera on our newly instantiated objects after creation.
        public [EditorWindow](EditorWindow.html) containerWindow { get; set; }
    
        // As this is ultimately just a [VisualElement](UIElements.VisualElement.html), it is appropriate to place initialization logic in the constructor.
        // In this method you can also register to any additional events as required. Here we will just set up the basics:
        // a tooltip, icon, and action.
        public CreateCubes()
        {
            // A toolbar element can be either text, icon, or a combination of the two. Keep in mind that if a toolbar is
            // docked horizontally the text will be clipped, so usually it's a good idea to specify an icon.
            text = "Create Cubes";
            icon = [AssetDatabase.LoadAssetAtPath](AssetDatabase.LoadAssetAtPath.html)<[Texture2D](Texture2D.html)>("Assets/CreateCubesIcon.png");
    
            tooltip = "Instantiate some cubes in the scene.";
            clicked += OnClick;
        }
    
        // This method will be invoked when the `CreateCubes` button is clicked.
        void OnClick()
        {
            var parent = new [GameObject](GameObject.html)("Cubes").transform;
    
            // When writing editor tools don't forget to be a good citizen and implement [Undo](Undo.html)!
            [Undo.RegisterCreatedObjectUndo](Undo.RegisterCreatedObjectUndo.html)(parent.gameObject, "Create Cubes in Sphere");
    
            for (int i = 0; i < 50; i++)
            {
                var cube = [GameObject.CreatePrimitive](GameObject.CreatePrimitive.html)([PrimitiveType.Cube](PrimitiveType.Cube.html)).transform;
    
                [Undo.RegisterCreatedObjectUndo](Undo.RegisterCreatedObjectUndo.html)(cube.gameObject, "Create Cubes in Sphere");
                cube.position = [Random.insideUnitSphere](Random-insideUnitSphere.html) * 25;
                cube.rotation = [Quaternion.LookRotation](Quaternion.LookRotation.html)([Random.onUnitSphere](Random-onUnitSphere.html));
    
                [Undo.SetTransformParent](Undo.SetTransformParent.html)(cube, parent, "Create Cubes in Sphere");
                cube.SetParent(parent);
            }
    
            [Selection.activeTransform](Selection-activeTransform.html) = parent;
    
            if (containerWindow is [SceneView](SceneView.html) view)
                view.FrameSelected();
        }
    }
    
    // Same as above, except this time we'll create a toggle + dropdown toolbar item.
    [EditorToolbarElement(id, typeof([SceneView](SceneView.html)))]
    class DropdownToggleExample : [EditorToolbarDropdownToggle](Toolbars.EditorToolbarDropdownToggle.html), [IAccessContainerWindow](Toolbars.IAccessContainerWindow.html)
    {
        public const string id = "ExampleToolbar/DropdownToggle";
    
        // This property is specified by [IAccessContainerWindow](Toolbars.IAccessContainerWindow.html) and is used to access the [Overlay](Overlays.Overlay.html)'s [EditorWindow](EditorWindow.html).
        public [EditorWindow](EditorWindow.html) containerWindow { get; set; }
        static int colorIndex = 0;
        static readonly [Color](Color.html)[] colors = new [Color](Color.html)[] { [Color.red](Color-red.html), [Color.green](Color-green.html), [Color.cyan](Color-cyan.html) };
    
        DropdownToggleExample()
        {
            text = "[Color](Color.html) Bar";
            tooltip = "[Display](Display.html) a color swatch in the top left of the scene view. [Toggle](UIElements.Toggle.html) on or off, and open the dropdown" +
                "to change the color.";
    
            // When the dropdown is opened, ShowColorMenu is invoked and we can create a popup menu.
            dropdownClicked += ShowColorMenu;
    
            // Subscribe to the [Scene](SceneManagement.Scene.html) View OnGUI callback so that we can draw our color swatch.
            [SceneView.duringSceneGui](SceneView-duringSceneGui.html) += DrawColorSwatch;
        }
    
        void DrawColorSwatch([SceneView](SceneView.html) view)
        {
            // Test that this callback is for the [Scene](SceneManagement.Scene.html) View that we're interested in, and also check if the toggle is on
            // or off (value).
            if (view != containerWindow || !value)
                return;
    
            [Handles.BeginGUI](Handles.BeginGUI.html)();
            [GUI.color](GUI-color.html) = colors[colorIndex];
            [GUI.DrawTexture](GUI.DrawTexture.html)(new [Rect](Rect.html)(8, 8, 120, 24), [Texture2D.whiteTexture](Texture2D-whiteTexture.html));
            [GUI.color](GUI-color.html) = [Color.white](Color-white.html);
            [Handles.EndGUI](Handles.EndGUI.html)();
        }
    
        // When the dropdown button is clicked, this method will create a popup menu at the mouse cursor position.
        void ShowColorMenu()
        {
            var menu = new [GenericMenu](GenericMenu.html)();
            menu.AddItem(new [GUIContent](GUIContent.html)("Red"), colorIndex == 0, () => colorIndex = 0);
            menu.AddItem(new [GUIContent](GUIContent.html)("Green"), colorIndex == 1, () => colorIndex = 1);
            menu.AddItem(new [GUIContent](GUIContent.html)("Blue"), colorIndex == 2, () => colorIndex = 2);
            menu.ShowAsContext();
        }
    }
    
    // All Overlays must be tagged with the [OverlayAttribute](Overlays.OverlayAttribute.html)
    [[Overlay](Overlays.Overlay.html)(typeof([SceneView](SceneView.html)), "Placement [Tools](Tools.html)")]
    // [IconAttribute](IconAttribute.html) provides a way to define an icon for when an [Overlay](Overlays.Overlay.html) is in collapsed form. If not provided, the first
    // two letters of the [Overlay](Overlays.Overlay.html) name will be used.
    [Icon("Assets/PlacementToolsIcon.png")]
    // [Toolbar](UIElements.Toolbar.html) overlays must inherit `[ToolbarOverlay](Overlays.ToolbarOverlay.html)` and implement a parameter-less constructor. The contents of a toolbar
    // are populated with string IDs, which are passed to the base constructor. IDs are defined by
    // [EditorToolbarElementAttribute](Toolbars.EditorToolbarElementAttribute.html).
    public class EditorToolbarExample : [ToolbarOverlay](Overlays.ToolbarOverlay.html)
    {
        // [ToolbarOverlay](Overlays.ToolbarOverlay.html) implements a parameterless constructor, passing 2 [EditorToolbarElementAttribute](Toolbars.EditorToolbarElementAttribute.html) IDs. This will
        // create a toolbar overlay with buttons for the CreateCubes and DropdownToggleExample examples.
        // This is the only code required to implement a toolbar overlay. Unlike panel overlays, the contents are defined
        // as standalone pieces that will be collected to form a strip of elements.
        EditorToolbarExample() : base(
            CreateCubes.id,
            DropdownToggleExample.id)
        {}
    }
    

### Properties

[toolbarElements](Overlays.ToolbarOverlay-toolbarElements.html)| Use
toolbarElements to specify the contents of this Overlay.  
---|---  
  
### Public Methods

[CreatePanelContent](Overlays.ToolbarOverlay.CreatePanelContent.html)| Creates
the root VisualElement of the ToolbarOverlay's content in panel layout.  
---|---  
  
### Inherited Members

### Static Properties

[ussClassName](Overlays.Overlay-ussClassName.html)| USS class name of elements
of this type.  
---|---  
  
### Properties

[collapsed](Overlays.Overlay-collapsed.html)| Defines whether the overlay is
in collapsed form.  
---|---  
[collapsedIcon](Overlays.Overlay-collapsedIcon.html)| Defines a custom icon to
use when that overlay is in collapsed form.  
[containerWindow](Overlays.Overlay-containerWindow.html)| EditorWindow the
overlay is contained within.  
[defaultSize](Overlays.Overlay-defaultSize.html)| Set defaultSize to define
the size of an Overlay when it hasn't been resized by the user.  
[displayed](Overlays.Overlay-displayed.html)| Shows or hides the overlay.  
[displayName](Overlays.Overlay-displayName.html)| Name of overlay used as
title.  
[floating](Overlays.Overlay-floating.html)| Returns true if overlay is
floating, returns false if overlay is docked in a corner or in a toolbar.  
[floatingPosition](Overlays.Overlay-floatingPosition.html)| Local position of
closest overlay corner to closest dockposition when floating.  
[id](Overlays.Overlay-id.html)| Overlay unique ID.  
[isInToolbar](Overlays.Overlay-isInToolbar.html)| Returns true if overlay is
docked in a toolbar.  
[layout](Overlays.Overlay-layout.html)| The preferred layout for the Overlay.  
[maxSize](Overlays.Overlay-maxSize.html)| Maximum size of the Overlay.  
[minSize](Overlays.Overlay-minSize.html)| Minimum size of the Overlay.  
[rootVisualElement](Overlays.Overlay-rootVisualElement.html)| The root
VisualElement.  
[size](Overlays.Overlay-size.html)| Size of the Overlay.  
  
### Public Methods

[Close](Overlays.Overlay.Close.html)| Remove the Overlay from its
OverlayCanvas.  
---|---  
[CreateContent](Overlays.Overlay.CreateContent.html)| Creates a new
VisualElement containing the contents of this Overlay.  
[OnCreated](Overlays.Overlay.OnCreated.html)| OnCreated is invoked when an
Overlay is instantiated in an Overlay Canvas.  
[OnWillBeDestroyed](Overlays.Overlay.OnWillBeDestroyed.html)| Called when an
Overlay is about to be destroyed.  
[RefreshPopup](Overlays.Overlay.RefreshPopup.html)| Resize the OverlayPopup to
fit the content.  
[Undock](Overlays.Overlay.Undock.html)| If this Overlay is currently in a
toolbar, it will be removed and return to a floating state.  
  
### Events

[collapsedChanged](Overlays.Overlay-collapsedChanged.html)| Invoked when
Overlay.collapsed value is changed.  
---|---  
[displayedChanged](Overlays.Overlay-displayedChanged.html)| This callback is
invoked when the Overlay.displayed value has been changed.  
[floatingChanged](Overlays.Overlay-floatingChanged.html)| Called when the
value of floating has changed.  
[floatingPositionChanged](Overlays.Overlay-floatingPositionChanged.html)| This
event is invoked when Overlay.floatingPosition is changed.  
[layoutChanged](Overlays.Overlay-layoutChanged.html)| Subscribe to this event
to be notified when the Overlay.Layout property is modified.  
  
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

