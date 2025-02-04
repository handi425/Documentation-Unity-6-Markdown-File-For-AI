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

# Overlay

class in UnityEditor.Overlays

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

Overlays are persistent and customizable panels and toolbars that are
available within Editor Windows. Use Overlays to expose actions and tool
options in a convenient and user-controllable way.

This is the base class that all overlays inherit from. To create an overlay,
return a UnityEngine.UIElements.VisualElement.  
  
The simplest way to display an overlay is to use
[OverlayAttribute](Overlays.OverlayAttribute.html) and register a target
[EditorWindow](EditorWindow.html).

    
    
    using [UnityEditor](UnityEditor.html);
    using UnityEditor.Overlays;
    using UnityEngine.UIElements;  
      
    // Specifying `[OverlayAttribute.editorWindowType](Overlays.OverlayAttribute-editorWindowType.html)` tells the [OverlayCanvas](Overlays.OverlayCanvas.html) to always show this [Overlay](Overlays.Overlay.html) in the menu.
    [[Overlay](Overlays.Overlay.html)(typeof([SceneView](SceneView.html)), "[Selection](Selection.html) Count")]
    class SelectionCount : [Overlay](Overlays.Overlay.html)
    {
        [Label](UIElements.Label.html) m_Label;  
      
        public override [VisualElement](UIElements.VisualElement.html) CreatePanelContent()
        {
            [Selection.selectionChanged](Selection-selectionChanged.html) += () =>
            {
                if (m_Label != null)
                    m_Label.text = $"[Selection](Selection.html) Count {[Selection.count](Selection-count.html)}";
            };  
      
            return m_Label = new [Label](UIElements.Label.html)($"[Selection](Selection.html) Count {[Selection.count](Selection-count.html)}");
        }
    }
    

Overlays can be used in any [EditorWindow](EditorWindow.html) that implements
[ISupportsOverlays](Overlays.ISupportsOverlays.html). You can use
[OverlayCanvas.Add](Overlays.OverlayCanvas.Add.html) and
[OverlayCanvas.Remove](Overlays.OverlayCanvas.Remove.html) to add and remove
overlays from the Overlays menu.

    
    
    using [System](Rendering.VirtualTexturing.System.html);
    using [UnityEditor](UnityEditor.html);
    using UnityEditor.Overlays;
    using UnityEngine;
    using UnityEngine.UIElements;  
      
    public class OverlayWindowExample : [EditorWindow](EditorWindow.html), [ISupportsOverlays](Overlays.ISupportsOverlays.html)
    {
        bool m_ShowOverlay;
        InstanceOverlay m_Overlay;  
      
        // InstanceOverlay is not registered as a persistent overlay, and it must be instantiated through code. In contrast,
        // PersistentOverlay is registered with a target window type and will be available at any time.
        // All [OverlayAttribute](Overlays.OverlayAttribute.html) properties are optional. Here, we specify that when this overlay is added to a window for the
        // first time, so it is visible by default. If defaultDisplay is set to it's default value of false, the
        // [Overlay](Overlays.Overlay.html) will be available in the [Overlay](Overlays.Overlay.html) [Menu](Menu.html) when added to a window, but not visible.
        [[Overlay](Overlays.Overlay.html)(defaultDisplay = true)]
        class InstanceOverlay : [Overlay](Overlays.Overlay.html)
        {
            OverlayWindowExample m_Window;
            public InstanceOverlay(OverlayWindowExample win) => m_Window = win;
            public override [VisualElement](UIElements.VisualElement.html) CreatePanelContent() => new [Label](UIElements.Label.html)() { text = $"Hello from {m_Window.name}!" };
        }  
      
        // Persistent overlays are always available in the [Overlay](Overlays.Overlay.html) [Menu](Menu.html). An [Overlay](Overlays.Overlay.html) is made persistent by assigning the
        // `editorWindowType` property in `[OverlayAttribute](Overlays.OverlayAttribute.html)`.
        [[Overlay](Overlays.Overlay.html)(typeof(OverlayWindowExample), "Persistent [Overlay](Overlays.Overlay.html)", defaultDisplay = true)]
        class PersistentOverlay : [Overlay](Overlays.Overlay.html)
        {
            public override [VisualElement](UIElements.VisualElement.html) CreatePanelContent() => new [Label](UIElements.Label.html)() { text = "Hello, I'm always available!" };
        }  
      
        [[MenuItem](MenuItem.html)("Window/[Overlay](Overlays.Overlay.html) Window")]
        static void Init() => GetWindow<OverlayWindowExample>();  
      
        void OnEnable() => m_Overlay = new InstanceOverlay(this);  
      
        void OnGUI()
        {
            [EditorGUI.BeginChangeCheck](EditorGUI.BeginChangeCheck.html)();
            m_ShowOverlay = [EditorGUILayout.Toggle](EditorGUILayout.Toggle.html)("Show [Overlay](Overlays.Overlay.html)", m_ShowOverlay);
            if ([EditorGUI.EndChangeCheck](EditorGUI.EndChangeCheck.html)())
            {
                if (m_ShowOverlay)
                    overlayCanvas.Add(m_Overlay);
                else
                    overlayCanvas.Remove(m_Overlay);
            }
        }
    }
    

Overlays can be shown in the active [SceneView](SceneView.html) through
[SceneView.AddOverlayToActiveView](SceneView.AddOverlayToActiveView.html) and
[SceneView.RemoveOverlayFromActiveView](SceneView.RemoveOverlayFromActiveView.html).
This is useful for [EditorTool](EditorTools.EditorTool.html)s that need to
show UI.

    
    
    using System.Linq;
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);
    using UnityEditor.EditorTools;
    using UnityEditor.Overlays;
    using UnityEngine.UIElements;  
      
    // A simple tool that moves the selected transforms using an [Overlay](Overlays.Overlay.html) interface.
    [[EditorTool](EditorTools.EditorTool.html)("Offset", typeof([Transform](Transform.html)))]
    public class OffsetTool : [EditorTool](EditorTools.EditorTool.html)
    {
        // By default, overlays added to the canvas are not displayed. Setting the `defaultDisplay` property ensures that the
        // first time this [Overlay](Overlays.Overlay.html) is added to a canvas it will be visible.
        [[Overlay](Overlays.Overlay.html)(defaultDisplay = true)]
        class OffsetToolOverlay : [Overlay](Overlays.Overlay.html)
        {
            [Transform](Transform.html)[] selection;  
      
            public OffsetToolOverlay([Transform](Transform.html)[] targets) => selection = targets;  
      
            public override [VisualElement](UIElements.VisualElement.html) CreatePanelContent()
            {
                var root = new [VisualElement](UIElements.VisualElement.html)();
                root.Add(new [Button](UIElements.Button.html)(() => Move([Vector3.right](Vector3-right.html))) { text = "Move Right" });
                root.Add(new [Button](UIElements.Button.html)(() => Move([Vector3.up](Vector3-up.html))) { text = "Move Up" });
                root.Add(new [Button](UIElements.Button.html)(() => Move([Vector3.forward](Vector3-forward.html))) { text = "Move Forward" });
                return root;
            }  
      
            void Move([Vector3](Vector3.html) direction)
            {
                [Undo.RecordObjects](Undo.RecordObjects.html)(selection, "Move [Selection](Selection.html)");
                foreach (var transform in selection)
                    transform.position += direction;
            }
        }  
      
        OffsetToolOverlay m_Overlay;  
      
        public override void OnActivated()
        {
            [SceneView.AddOverlayToActiveView](SceneView.AddOverlayToActiveView.html)(m_Overlay = new OffsetToolOverlay(targets.Select(x => x as [Transform](Transform.html)).ToArray()));
        }  
      
        public override void OnWillBeDeactivated()
        {
            [SceneView.RemoveOverlayFromActiveView](SceneView.RemoveOverlayFromActiveView.html)(m_Overlay);
        }
    }
    

To create an Overlay that is dockable in a toolbar, see
[ToolbarOverlay](Overlays.ToolbarOverlay.html).

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
[CreatePanelContent](Overlays.Overlay.CreatePanelContent.html)| Implement this
method to return your visual element content.  
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

