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

# UnityEditor

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

The UnityEditor assembly implements the editor-specific APIs in Unity. It
cannot be referenced by runtime code compiled into players.

### Classes

[AddAndRemoveRequest](PackageManager.Requests.AddAndRemoveRequest.html)|
Represents an asynchronous request to add package dependencies to the project
and/or remove package dependencies from the project.  
---|---  
[AddedComponent](SceneManagement.AddedComponent.html)| Class with information
about a component that has been added to a Prefab instance.  
[AddedGameObject](SceneManagement.AddedGameObject.html)| Class with
information about a GameObject that has been added as a child under a Prefab
instance.  
[AddRequest](PackageManager.Requests.AddRequest.html)| Represents an
asynchronous request to add a package to the project.  
[AdvancedDropdown](IMGUI.Controls.AdvancedDropdown.html)| Inherit from this
class to implement your own drop-down control.  
[AdvancedDropdownItem](IMGUI.Controls.AdvancedDropdownItem.html)| Items that
build the drop-down list.  
[AdvancedDropdownState](IMGUI.Controls.AdvancedDropdownState.html)| The state
of the drop-down. This Object can be serialized.  
[AdvancedObjectSelectorAttribute](SearchService.AdvancedObjectSelectorAttribute.html)|
This attribute lets you register a custom advanced object selector.  
[AdvancedObjectSelectorValidatorAttribute](SearchService.AdvancedObjectSelectorValidatorAttribute.html)|
This attribute lets you register a custom advanced object selector validator.  
[AdvertisementSettings](Advertisements.AdvertisementSettings.html)| Editor API
for the Unity Services editor feature. Normally UnityAds is enabled from the
Services window, but if writing your own editor extension, this API can be
used.  
[AnalyticsSettings](Analytics.AnalyticsSettings.html)| Editor API for the
Unity Services editor feature. Normally Analytics is enabled from the Services
window, but if writing your own editor extension, this API can be used.  
[AndroidAssetPackImporter](AndroidAssetPackImporter.html)| Represents an
Android asset pack directory in a project.  
[AnimationClipCurveData](AnimationClipCurveData.html)| An
AnimationClipCurveData object contains all the information needed to identify
a specific curve in an AnimationClip. The curve animates a specific property
of a component / material attached to a game object / animated bone.  
[AnimationMode](AnimationMode.html)|  AnimationMode is used by the
AnimationWindow to store properties modified by the AnimationClip playback.  
[AnimationModeDriver](AnimationModeDriver.html)|  AnimationMode uses
AnimationModeDriver to identify the animation driver.  
[AnimationUtility](AnimationUtility.html)| Editor utility functions for
modifying animation clips.  
[AnimationWindow](AnimationWindow.html)| Use the AnimationWindow class to
select and edit Animation clips.  
[AnimatorController](Animations.AnimatorController.html)| The Animator
Controller controls animation through layers with state machines, controlled
by parameters.  
[AnimatorControllerLayer](Animations.AnimatorControllerLayer.html)| The
Animation Layer contains a state machine that controls animations of a model
or part of it.  
[AnimatorState](Animations.AnimatorState.html)| States are the basic building
blocks of a state machine. Each state contains a Motion ( AnimationClip or
BlendTree) which will play while the character is in that state. When an event
in the game triggers a state transition, the character will be left in a new
state whose animation sequence will then take over.  
[AnimatorStateMachine](Animations.AnimatorStateMachine.html)| A graph
controlling the interaction of states. Each state references a motion.  
[AnimatorStateTransition](Animations.AnimatorStateTransition.html)|
Transitions define when and how the state machine switch from one state to
another. AnimatorStateTransition always originate from an Animator State (or
AnyState) and have timing parameters.  
[AnimatorTransition](Animations.AnimatorTransition.html)| Transitions define
when and how the state machine switch from on state to another.
AnimatorTransition always originate from a StateMachine or a StateMachine
entry. They do not define timing parameters.  
[AnimatorTransitionBase](Animations.AnimatorTransitionBase.html)| Base class
for animator transitions. Transitions define when and how the state machine
switches from one state to another.  
[AnimBool](AnimatedValues.AnimBool.html)| Lerp from 0 - 1.  
[AnimFloat](AnimatedValues.AnimFloat.html)| An animated float value.  
[AnimQuaternion](AnimatedValues.AnimQuaternion.html)| An animated Quaternion
value.  
[AnimVector3](AnimatedValues.AnimVector3.html)| An animated Vector3 value.  
[ApplicationTitleDescriptor](ApplicationTitleDescriptor.html)| Utility class
containing all the information necessary to format Unity Editor main window
title. All the various fields are concatenated to create a fully formed title.
If only ApplicationTitleDescriptor.title is provided, this will become the
complete title.  
[ApplyRulesIfGraphicsAPIAttribute](ShaderKeywordFilter.ApplyRulesIfGraphicsAPIAttribute.html)|
Enable or disable shader keyword filter attributes based on the graphics API.  
[ApplyRulesIfNotGraphicsAPIAttribute](ShaderKeywordFilter.ApplyRulesIfNotGraphicsAPIAttribute.html)|
Enable or disable shader keyword filter attributes based on the graphics API.  
[ApplyRulesIfTagsEqualAttribute](ShaderKeywordFilter.ApplyRulesIfTagsEqualAttribute.html)|
Enable or disable shader keyword filter attributes based on shader tags.  
[ApplyRulesIfTagsNotEqualAttribute](ShaderKeywordFilter.ApplyRulesIfTagsNotEqualAttribute.html)|
Enable or disable shader keyword filter attributes based on shader tags.  
[ArcHandle](IMGUI.Controls.ArcHandle.html)| A class for a compound handle to
edit an angle and a radius in the Scene view.  
[ArrayUtility](ArrayUtility.html)| Helpers for builtin arrays.  
[Assembly](Compilation.Assembly.html)| Class that represents an assembly
compiled by Unity.  
[AssemblyDefinitionException](Compilation.AssemblyDefinitionException.html)|
An exception throw for Assembly Definition Files errors.  
[AssemblyReloadEvents](AssemblyReloadEvents.html)| This class has event
dispatchers for assembly reload events.  
[Asset](VersionControl.Asset.html)| This class containes information about the
version control state of an asset.  
[AssetBundleInfo](Build.Content.AssetBundleInfo.html)| Container for holding
asset loading information for an AssetBundle to be built.  
[AssetDatabase](AssetDatabase.html)| An Interface for accessing assets and
performing operations on assets.  
[AssetDatabaseLoadOperation](AssetDatabaseLoadOperation.html)| This operation
allows you to track the progress and access the result of an asynchronus
AssetDatabase load operation.  
[AssetImportContext](AssetImporters.AssetImportContext.html)| Defines the
import context for scripted importers during an import event.  
[AssetImporter](AssetImporter.html)| Base class from which asset importers for
specific asset types derive.  
[AssetImporterEditor](AssetImporters.AssetImporterEditor.html)| Default editor
for all asset importer settings.  
[AssetList](VersionControl.AssetList.html)| A list of version control
information about assets.  
[AssetLoadInfo](Build.Content.AssetLoadInfo.html)| Container for holding
preload information for a given serialized Asset.  
[AssetModificationProcessor](AssetModificationProcessor.html)|
AssetModificationProcessor lets you hook into saving of serialized assets and
scenes which are edited inside Unity.  
[AssetMonitoringUtilities](UIElements.AssetMonitoringUtilities.html)| Utility
that manages asset monitoring features of UI Toolkit panels.  
[AssetPostprocessor](AssetPostprocessor.html)| AssetPostprocessor lets you
hook into the import pipeline and run scripts prior or after importing assets.  
[AssetPostprocessorStaticVariableIgnoreAttribute](AssetPostprocessorStaticVariableIgnoreAttribute.html)|
Allows you to decorate static variables in AssetPostprocessor and
ScriptedImporter classes that should be ignored by the static variable warning
system in the Import Activity window.This attribute is introduced to decorate
static variables in PostProcessors and ScripttedImporters to prevent warnings
about the usage of static variables. Though static variables in these classes
can lead to subtle bugs when running on different Asset Import Workers as each
worker has its own Mono Domain separate from the Main Editor, this attribute
has been added to reduce the noise which could be generated in some difficult
to fix situations involving static variables in said clasess.  
[AssetPreview](AssetPreview.html)| Utility for fetching asset previews by
instance ID of assets, See AssetPreview.GetAssetPreview. Since previews are
loaded asynchronously methods are provided for requesting if all previews have
been fully loaded, see AssetPreview.IsLoadingAssetPreviews. Loaded previews
are stored in a cache, the size of the cache can be controlled by calling
[AssetPreview.SetPreviewTextureCacheSize].  
[AssetSettingsProvider](AssetSettingsProvider.html)| AssetSettingsProvider is
a specialization of the SettingsProvider class that converts legacy settings
to Unified Settings. Legacy settings include any settings that used the
Inspector to modify themselves, such as the *.asset files under the
ProjectSettings folder. Under the hood, AssetSettingsProvider creates an
Editor for specific Assets and builds the UI for the Settings window by
wrapping the Editor.OnInspectorGUI function.Internally we use this class to
wrap our existing settings.  
[Attacher](Experimental.GraphView.Attacher.html)| Helper object that attaches
a visual element next to its target, regarless of their respective location in
the visual tree hierarchy.  
[AudioCurveRendering](AudioCurveRendering.html)| Antialiased curve rendering
functionality used by audio tools in the editor.  
[AudioImporter](AudioImporter.html)| Audio importer lets you modify AudioClip
import settings from editor scripts.  
[AuthorInfo](PackageManager.AuthorInfo.html)| Identifies the author of a
package.  
[BakeProgressState](LightTransport.BakeProgressState.html)| Interface for
progress reporting.  
[BaseAnimValue<T0>](AnimatedValues.BaseAnimValue_1.html)| Abstract base class
for Animated Values.  
[BaseAnimValueNonAlloc<T0>](AnimatedValues.BaseAnimValueNonAlloc_1.html)|
Abstract base class that provides an allocation free version of BaseAnimValue.  
[BaseMaskField<T0>](UIElements.BaseMaskField_1.html)|  Base class implementing
the shared functionality for editing bit mask values. For more information,
refer to UXML element MaskField.  
[BindingExtensions](UIElements.BindingExtensions.html)|  Provides
VisualElement extension methods that implement data binding between
INotifyValueChanged fields and SerializedObjects.  
[Blackboard](Experimental.GraphView.Blackboard.html)| GraphElement that
enables user to dynamically define members of a Graph (such as
fields/properties) grouped by sections (BlackboardSection).  
[BlackboardField](Experimental.GraphView.BlackboardField.html)| GraphElement
that represents a field of a Graph.  
[BlackboardRow](Experimental.GraphView.BlackboardRow.html)| Collapsible
GraphElement that represents a row in a BlackboardSection.  
[BlackboardSection](Experimental.GraphView.BlackboardSection.html)|
GraphElement that represents a section of members in a Blackboard.  
[BlendTree](Animations.BlendTree.html)| Blend trees are used to blend
continuously animation between their children. They can either be 1D or 2D.  
[BoxBoundsHandle](IMGUI.Controls.BoxBoundsHandle.html)| A compound handle to
edit a box-shaped bounding volume in the Scene view.  
[BrokenPrefabAsset](BrokenPrefabAsset.html)| BrokenPrefabAsset is for Prefab
files where the file content cannot be loaded without errors.  
[BrushesOverlay](TerrainTools.BrushesOverlay.html)| Contains functions that
help display Terrain Tools overlays.  
[BuildCallbackVersionAttribute](Build.BuildCallbackVersionAttribute.html)|
Attribute to provide a version number for IProcessSceneWithReport callbacks.  
[BuildFailedException](Build.BuildFailedException.html)| An exception class
that represents a failed build.  
[BuildPipeline](BuildPipeline.html)| Lets you programmatically build players
or AssetBundles which can be loaded from the web.  
[BuildPipelineContext](Build.BuildPipelineContext.html)| Defines the build
context for IProcessSceneWithReport during a build event.  
[BuildPlayerContext](Build.BuildPlayerContext.html)| Get a BuildPlayerContext
object from a BuildPlayerProcessor.PrepareForBuild callback.  
[BuildPlayerProcessor](Build.BuildPlayerProcessor.html)| Extend
BuildPlayerProcessor to receive callbacks during a player build.  
[BuildPlayerWindow](BuildPlayerWindow.html)| The default build settings
window.  
[BuildProfile](Build.Profile.BuildProfile.html)| Provides a set of
configuration settings you can use to build your application on a particular
platform.  
[BuildReferenceMap](Build.Content.BuildReferenceMap.html)| Container for
holding information about where objects will be serialized in a build.  
[BuildReport](Build.Reporting.BuildReport.html)| The BuildReport API gives you
information about the Unity build process.  
[BuildUsageCache](Build.Content.BuildUsageCache.html)| Caching object for the
Scriptable Build Pipeline.  
[BuildUsageTagSet](Build.Content.BuildUsageTagSet.html)| Container for holding
information about how objects are being used in a build.  
[BuildUtilities](PackageManager.BuildUtilities.html)| Utility class that
allows packages to register build callbacks with the Unity Package Manager.  
[CacheServer](CacheServer.html)| This class provides an interface for
performing operations on a cache server.  
[CallbackOrderAttribute](CallbackOrderAttribute.html)| Base class for
Attributes that require a callback index.  
[CameraDescription](AssetImporters.CameraDescription.html)| Represents camera
information from an imported file.  
[CameraEditor](CameraEditor.html)| Unity Camera Editor.  
[CameraEditorUtils](CameraEditorUtils.html)| Utilities for cameras.  
[CanEditMultipleObjects](CanEditMultipleObjects.html)| Attribute used to make
a custom editor support multi-object editing.  
[CapsuleBoundsHandle](IMGUI.Controls.CapsuleBoundsHandle.html)| A compound
handle to edit a capsule-shaped bounding volume in the Scene view.  
[ChangeSet](VersionControl.ChangeSet.html)| Wrapper around a changeset
description and ID.  
[ChangeSets](VersionControl.ChangeSets.html)| A list of the ChangeSet class.  
[ChannelClient](MPE.ChannelClient.html)| ChannelClient is a WebSocket client
that connects to Unity's ChannelService, which is a WebSocket server.  
[ChannelService](MPE.ChannelService.html)| The ChannelService encapsulates a
WebSocket server running in Unity.  
[ClearCacheRequest](PackageManager.Requests.ClearCacheRequest.html)|
Represents an asynchronous request to clear the global package cache on the
disk.  
[ClickSelector](Experimental.GraphView.ClickSelector.html)| Selects element on
single click.  
[Client](PackageManager.Client.html)| Use the Unity Package Manager Client
class to manage the packages used in a project.  
[ClipboardUtility](ClipboardUtility.html)| A class containing methods to
assist with clipboard operations.  
[CloudProjectSettings](CloudProjectSettings.html)| Use this class to retrieve
information about the currently selected project and the current Unity ID that
is logged in.  
[CloudProjectSettingsEventManager](CloudProjectSettingsEventManager.html)|
Manages the events related to the project state.  
[ClutchShortcutAttribute](ShortcutManagement.ClutchShortcutAttribute.html)|
Registers a static method as the action for a clutch shortcut.  
[CodeEditor](Unity.CodeEditor.CodeEditor.html)| Handles interaction with the
code editor.  
[CollectImportedDependenciesAttribute](AssetImporters.CollectImportedDependenciesAttribute.html)|
Use this method attribute to specify which methods declare dependancies on
imported assets. The methods are called by AssetDatabase during import.  
[ColorField](UIElements.ColorField.html)|  Makes a field for selecting a
color. For more information, refer to UXML element ColorField.  
[ColorPickerHDRConfig](ColorPickerHDRConfig.html)| Used as input to ColorField
to configure the HDR color ranges in the ColorPicker.  
[CommonRoles](Build.Reporting.CommonRoles.html)| This class provides constant
values for some of the common roles used by files in the build. The role of
each file in the build is available in BuildFile.role.  
[CompilationPipeline](Compilation.CompilationPipeline.html)| Methods and
properties for script compilation pipeline.  
[ComputeShaderImporter](ComputeShaderImporter.html)| Define compute shader
import settings in the Unity Editor.  
[ConfigField](VersionControl.ConfigField.html)| Describes the configuration
fields of the version control that the user has selected in the Unity Editor.  
[ConnectedPlayer](Networking.PlayerConnection.ConnectedPlayer.html)|
Information of the connected player.  
[ConsoleWindowUtility](ConsoleWindowUtility.html)| Console Window Utility
class.  
[ContentBuildInterface](Build.Content.ContentBuildInterface.html)| Low level
interface for building content for Unity.  
[ContentDragger](Experimental.GraphView.ContentDragger.html)| Manipulator that
allows mouse-dragging of one or more elements.  
[ContentZoomer](Experimental.GraphView.ContentZoomer.html)| Manipulator that
allows zooming in GraphView.  
[ContextMenuUtility](Actions.ContextMenuUtility.html)| Provides methods to add
menu items to the Scene view context menu.  
[ConvertToPrefabInstanceSettings](ConvertToPrefabInstanceSettings.html)|
Settings controlling the behavior of PrefabUtility.ConvertToPrefabInstance.  
[CoppaDrawer](Connect.CoppaDrawer.html)| A container that fetches the
UIElements that draw the COPPA compliance UI and subscribes to its events.  
[CrashReportingSettings](CrashReporting.CrashReportingSettings.html)| Editor
API for the Unity Services editor feature. Normally CrashReporting is enabled
from the Services window, but if writing your own editor extension, this API
can be used.  
[CurveField](UIElements.CurveField.html)|  Makes a field for editing an
AnimationCurve. For more information, refer to UXML element CurveField.  
[CustomEditor](CustomEditor.html)| Tells an Editor class which run-time type
it's an editor for.  
[CustomObjectIndexerAttribute](Search.CustomObjectIndexerAttribute.html)|
Allows a user to register a custom Indexing function for a specific type.  
[CustomPreviewAttribute](CustomPreviewAttribute.html)| Adds an extra preview
in the Inspector for the specified type.  
[CustomPropertyDrawer](CustomPropertyDrawer.html)| Tells a custom
PropertyDrawer or DecoratorDrawer which run-time Serializable class or
PropertyAttribute it's a drawer for.  
[DecoratorDrawer](DecoratorDrawer.html)| Base class to derive custom decorator
drawers from.  
[DefaultAsset](DefaultAsset.html)| DefaultAsset is used for assets that do not
have a specific type (yet).  
[DefaultLightingExplorerExtension](DefaultLightingExplorerExtension.html)|
Default definition for the Lighting Explorer. Can be overridden completely or
partially.  
[DependencyInfo](SceneTemplate.DependencyInfo.html)| A descriptor that stores
one of a template Scene's dependency Assets, and specifies whether to clone or
reference it when the template is instantiated.  
[DetailBrushRepresentation](TerrainTools.DetailBrushRepresentation.html)|
Represents data associated with the brush used for scattering details.  
[DeviceSimulator](DeviceSimulation.DeviceSimulator.html)| Class for
interacting with a Device Simulator window from a script.  
[DeviceSimulatorPlugin](DeviceSimulation.DeviceSimulatorPlugin.html)| Extend
this class to create a Device Simulator plug-in.  
[DidReloadScripts](Callbacks.DidReloadScripts.html)| Add this attribute to a
method to get a notification after scripts have been reloaded.  
[DiffuseProfileCallbackAttribute](SpeedTree.Importer.DiffuseProfileCallbackAttribute.html)|
This attribute is used as a callback to set SRP specific properties from the
importer.  
[Dispatcher](Search.Dispatcher.html)| The search dispatcher is used to
synchronize events from the search provider threads and the main UI threads.  
[DragAndDrop](DragAndDrop.html)| Editor drag & drop operations.  
[Dragger](Experimental.GraphView.Dragger.html)| Base manipulator for mouse-
dragging elements.  
[DrawGizmo](DrawGizmo.html)| The DrawGizmo attribute allows you to supply a
gizmo renderer for any Component.  
[Edge](Experimental.GraphView.Edge.html)| The GraphView edge element.  
[EdgeConnector](Experimental.GraphView.EdgeConnector.html)| Manipulator for
creating new edges.  
[EdgeConnector<T0>](Experimental.GraphView.EdgeConnector_1.html)| Manipulator
for creating new edges.  
[EdgeControl](Experimental.GraphView.EdgeControl.html)| VisualElement that
draws the edge lines and detects if mouse is on top of edge.  
[EdgeDragHelper](Experimental.GraphView.EdgeDragHelper.html)| EdgeDragHelper's
constructor.  
[EdgeDragHelper<T0>](Experimental.GraphView.EdgeDragHelper_1.html)| Edge drag
helper class.  
[EdgeManipulator](Experimental.GraphView.EdgeManipulator.html)| Edge
manipulator used to drag edges off ports and reconnect them elsewhere.  
[Editor](Editor.html)| Derive from this base class to create a custom
inspector or editor for your custom object.  
[EditorAction](Actions.EditorAction.html)| An EditorAction is a temporary tool
that can represent either an atomic action or an interactive utility.  
[EditorAnalytics](EditorAnalytics.html)| Editor API for the EditorAnalytics
feature.  
[EditorAnalyticsSessionInfo](EditorAnalyticsSessionInfo.html)| Provides access
to Editor Analytics session information.  
[EditorApplication](EditorApplication.html)| Main Application class.  
[EditorBuildSettings](EditorBuildSettings.html)| This class allows you to
modify the Editor Build Settings via script.  
[EditorBuildSettingsScene](EditorBuildSettingsScene.html)| Represents entries
in the Scenes list, as displayed in the Build Settings window.  
[EditorCameraUtils](Rendering.EditorCameraUtils.html)| Utilities for Camera
rendering in the Editor.  
[EditorConnection](Networking.PlayerConnection.EditorConnection.html)| Handles
the connection from the Editor to the Player.  
[EditorGraphicsSettings](Rendering.EditorGraphicsSettings.html)| Editor-
specific script interface for Graphics Settings.  
[EditorGUI](EditorGUI.html)| These work pretty much like the normal GUI
functions - and also have matching implementations in EditorGUILayout.  
[EditorGUILayout](EditorGUILayout.html)| Auto laid out version of EditorGUI.  
[EditorGUIUtility](EditorGUIUtility.html)| Miscellaneous helper stuff for
EditorGUI.  
[EditorJsonUtility](EditorJsonUtility.html)| Utility functions for working
with JSON data and engine objects.  
[EditorPrefs](EditorPrefs.html)| Stores and accesses Unity Editor preferences.  
[EditorSceneManager](SceneManagement.EditorSceneManager.html)| Scene
management in the Editor.  
[EditorSettings](EditorSettings.html)| User settings for Unity Editor.  
[EditorSnapSettings](EditorSnapSettings.html)| Control the behavior of handle
snapping in the editor.  
[EditorStyles](EditorStyles.html)| Common GUIStyles used for EditorGUI
controls.  
[EditorTool](EditorTools.EditorTool.html)| Use this class to implement editor
tools. This is the base class from which all editor tools are inherited.  
[EditorToolAttribute](EditorTools.EditorToolAttribute.html)| Registers an
EditorTool as either a Global tool or a Component tool for a specific target
type.  
[EditorToolbarButton](Toolbars.EditorToolbarButton.html)| A clickable button
used with EditorToolbarElementAttribute.  
[EditorToolbarDropdown](Toolbars.EditorToolbarDropdown.html)| A clickable
dropdown used with EditorToolbarElementAttribute.  
[EditorToolbarDropdownToggle](Toolbars.EditorToolbarDropdownToggle.html)| A
control that is both a toggle and a dropdown used with
EditorToolbarElementAttribute.  
[EditorToolbarElementAttribute](Toolbars.EditorToolbarElementAttribute.html)|
The EditorToolbarElement attribute allows you to make available a specific
VisualElement for use in an Editor Toolbar.  
[EditorToolbarFloatField](Toolbars.EditorToolbarFloatField.html)| A float
field used with EditorToolbarElementAttribute.  
[EditorToolbarToggle](Toolbars.EditorToolbarToggle.html)| A toggle used with
EditorToolbarElementAttribute.  
[EditorToolbarUtility](Toolbars.EditorToolbarUtility.html)| Editor utility
functions when working with EditorToolbar.  
[EditorToolContext](EditorTools.EditorToolContext.html)| Use this class to
implement specialized versions of the built-in transform tools. Built-in
transform tools include Move, Rotate, Scale, Rect, and Transform.  
[EditorToolContextAttribute](EditorTools.EditorToolContextAttribute.html)|
Registers an EditorToolContext as either a global context or a Component
context for a specific target type.  
[EditorUserBuildSettings](EditorUserBuildSettings.html)| User build settings
for the Editor  
[EditorUtility](EditorUtility.html)| Editor utility functions.  
[EditorWindow](EditorWindow.html)| Derive from this class to create a custom
Editor window.  
[EditorWindowTitleAttribute](EditorWindowTitleAttribute.html)| Use this class
to set title text and icon for an Editor window.  
[EmbedRequest](PackageManager.Requests.EmbedRequest.html)| Represents an
asynchronous request to embed a package inside a project.  
[EndNameEditAction](ProjectWindowCallback.EndNameEditAction.html)| Base class
to implement callbacks to be used when creating assets via the project window.
You can extend the EndNameEditAction and write your own callback.  
[EntitlementGroupInfo](Experimental.Licensing.EntitlementGroupInfo.html)| Data
structure for entitlement group information (often synonymous with a license
file), accessed through EntitlementInfo.  
[EntitlementInfo](Experimental.Licensing.EntitlementInfo.html)| Data structure
for an individual entitlement, the results of a call to
LicensingUtility.HasEntitlementsExtended.  
[EnumFlagsField](UIElements.EnumFlagsField.html)|  Makes a dropdown for
switching between enum flag values that are marked with the Flags attribute.  
[Error](PackageManager.Error.html)| Structure describing the error of a
package operation.  
[Events](PackageManager.Events.html)| An Interface for accessing the package
manager events.  
[EventService](MPE.EventService.html)| The EventService is a singleton
implementation of a ChannelClient that runs on all instances of Unity. It is
connected to the "events" channel and allows a Unity instance to send JSON
messages to other EventServices in external process, or other instances of
Unity.  
[FBXMaterialDescriptionPreprocessor](AssetImporters.FBXMaterialDescriptionPreprocessor.html)|
This is a default implementation for
AssetPostProcessor.OnPreprocessMaterialDescription, this implementation
converts material descriptions imported from FBX assets into materials for the
internal rendering pipeline.  
[FilePathAttribute](FilePathAttribute.html)| An attribute that specifies a
file location relative to the Project folder or Unity's preferences folder.
Additional resources: Location.  
[FileUtil](FileUtil.html)| Lets you do move, copy, delete operations over
files or directories.  
[FilterAttribute](ShaderKeywordFilter.FilterAttribute.html)| Tell the shader
system which shader keywords to include or remove from the build, based on the
data field underneath.  
[FrameDataView](Profiling.FrameDataView.html)| Base funtionality for accessing
the Profiler data.  
[FreehandSelector](Experimental.GraphView.FreehandSelector.html)| Freehand
selection tool.  
[FuzzySearch](Search.FuzzySearch.html)| Provides a method to match query text
using a fuzzy search algorithm.  
[GameObjectRecorder](Animations.GameObjectRecorder.html)| Records the changing
properties of a GameObject as the Scene runs and saves the information into an
AnimationClip.  
[GameObjectToolContext](EditorTools.GameObjectToolContext.html)| This class
represents the default context for manipulation tools. When
GameObjectToolContext is active, manipulation tools affect the transform
property of GameObjects in the SceneView Selection.  
[GameObjectUtility](GameObjectUtility.html)| GameObject utility functions.  
[GenericMenu](GenericMenu.html)| GenericMenu lets you create custom context
menus and dropdown menus.  
[GitInfo](PackageManager.GitInfo.html)| Identifies a specific revision for a
Git package using a Git commit hash.  
[GizmoInfo](GizmoInfo.html)| GizmoInfo contains information about the Scene
View gizmo and icon for a component type.  
[GizmoUtility](GizmoUtility.html)| A static class for interacting with the
Scene View icons and gizmos for types.  
[GradientField](UIElements.GradientField.html)|  Makes a field for editing an
Gradient. For more information, refer to UXML element GradientField.  
[GraphElement](Experimental.GraphView.GraphElement.html)| Base class for main
GraphView VisualElements.  
[GraphElementScopeExtensions](Experimental.GraphView.GraphElementScopeExtensions.html)|
Set of extension methods useful for Scope.  
[GraphicsAPIConstraintAttribute](ShaderKeywordFilter.GraphicsAPIConstraintAttribute.html)|
Enable or disable shader keyword filter attributes based on the graphics API.  
[GraphicsSettingsInspectorUtility](Inspector.GraphicsSettingsInspectors.GraphicsSettingsInspectorUtility.html)|
Utility class for GraphicsSettings page.  
[GraphView](Experimental.GraphView.GraphView.html)| Main GraphView class.  
[GraphViewBlackboardWindow](Experimental.GraphView.GraphViewBlackboardWindow.html)|
The base class for a floating window that contains a Blackboard.  
[GraphViewEditorWindow](Experimental.GraphView.GraphViewEditorWindow.html)|
Abstract base class for an editor window that contains a GraphView.  
[GraphViewMinimapWindow](Experimental.GraphView.GraphViewMinimapWindow.html)|
A floating window containing a MiniMap.  
[GraphViewToolWindow](Experimental.GraphView.GraphViewToolWindow.html)|
Abstract base class for a GraphView tool window.  
[GridBackground](Experimental.GraphView.GridBackground.html)| Default
GraphView background.  
[GridPalette](GridPalette.html)| GridPalette stores settings for Palette
assets when shown in the Palette window.  
[Group](Experimental.GraphView.Group.html)| Allows interactive insertion of
elements in a named scope.  
[GUIDrawer](GUIDrawer.html)| Base class for PropertyDrawer and
DecoratorDrawer.  
[Handles](Handles.html)| Custom 3D GUI controls and drawing in the Scene view.  
[HandleUtility](HandleUtility.html)| Helper functions for Scene View style 3D
GUI.  
[Help](Help.html)| Helper class to access Unity documentation.  
[HierarchyFrameDataView](Profiling.HierarchyFrameDataView.html)| Provides
access to the Profiler data for a specific frame and thread.  
[Highlighter](Highlighter.html)| Use this class to highlight elements in the
editor for use in in-editor tutorials and similar.  
[HyperLinkClickedEventArgs](HyperLinkClickedEventArgs.html)| Arguments for the
event EditorGUI.hyperLinkClicked.  
[IconBadge](Experimental.GraphView.IconBadge.html)| A rectangular badge,
usually attached to another visual element.  
[IHVImageFormatImporter](IHVImageFormatImporter.html)| Use
IHVImageFormatImporter to modify Texture2D import settings for Textures in IHV
(Independent Hardware Vendor) formats such as .DDS and .PVR from Editor
scripts.  
[IMGUIOverlay](Overlays.IMGUIOverlay.html)| IMGUIOverlay is an implementation
of Overlay that provides a IMGUIContainer.  
[ImportLog](AssetImporters.ImportLog.html)| Container class that holds the
collection of logs generated by an importer during the import process.  
[InitializeOnEnterPlayModeAttribute](InitializeOnEnterPlayModeAttribute.html)|
Allow an editor class method to be initialized when Unity enters Play Mode.  
[InitializeOnLoadAttribute](InitializeOnLoadAttribute.html)| Allows you to
initialize an Editor class when Unity loads, and when your scripts are
recompiled.  
[InitializeOnLoadMethodAttribute](InitializeOnLoadMethodAttribute.html)| Allow
an editor class method to be initialized when Unity loads without action from
the user.  
[InputExtraction](LightTransport.InputExtraction.html)| Class used when
extracting BakeInput from the set of open scenes.  
[InSceneAssetUtility](InSceneAssetUtility.html)| Provides methods related to
in-scene assets.  
[InspectorElement](UIElements.InspectorElement.html)|  Create a VisualElement
inspector from a SerializedObject.  
[InstantiationResult](SceneTemplate.InstantiationResult.html)| A class that
holds the data created when a SceneTemplateAsset is instantiated.  
[IntegrationContext](LightTransport.IntegrationContext.html)| Interface for
integration-specific data.  
[iOSDeviceRequirement](iOSDeviceRequirement.html)| A device requirement
description used for configuration of App Slicing.  
[ItemSelectors](Search.ItemSelectors.html)| Utility class to generate search
column with item selectors.  
[JointAngularLimitHandle](IMGUI.Controls.JointAngularLimitHandle.html)| A
class for a compound handle to edit multiaxial angular motion limits in the
Scene view.  
[L10n](L10n.html)| Class for text localization.  
[LayerField](UIElements.LayerField.html)|  A LayerField editor. For more
information, refer to UXML element LayerField.  
[LayerMaskField](UIElements.LayerMaskField.html)|  A LayerMaskField editor.
For more information, refer to UXML element LayerMaskField.  
[LicensingUtility](Experimental.Licensing.LicensingUtility.html)| Use the
Licensing Utility class to request user permissions. User permissions are
referred to as entitlements, which are simple strings, ie.
"com.unity.editor.ui".  
[LightDescription](AssetImporters.LightDescription.html)| Represents light
information from an imported file.  
[LightEditor](LightEditor.html)| The class used to render the Light Editor
when a Light is selected in the Unity Editor.  
[LightingDataAsset](LightingDataAsset.html)| The lighting data asset used by
the active Scene.  
[LightingExplorerTab](LightingExplorerTab.html)| Create custom tabs for the
Lighting Explorer.  
[LightingExplorerTableColumn](LightingExplorerTableColumn.html)| This is used
when defining how a column should look and behave in the Lighting Explorer.  
[LightingWindowEnvironmentSection](LightingWindowEnvironmentSection.html)|
Base class for the Inspector that overrides the Environment section of the
Lighting window.  
[LightingWindowTab](LightingWindowTab.html)| Base class to add custom tabs to
the Lighting window.  
[LightmapEditorSettings](LightmapEditorSettings.html)| This class is now
obsolete. Use LightingSettings.  
[LightmapParameters](LightmapParameters.html)| Configures how Unity bakes
lighting and can be assigned to a LightingSettings instance or asset.  
[Lightmapping](Lightmapping.html)| Allows to control the lightmapping job.  
[Lightmapping](Experimental.Lightmapping.html)| Experimental lightmapping
features.  
[ListRequest](PackageManager.Requests.ListRequest.html)| Represents an
asynchronous request to list the packages in the project.  
[LocalizationAttribute](LocalizationAttribute.html)| An attribute to the
assembly for Localization.  
[LocalizationGroup](LocalizationGroup.html)| This provides an auto dispose
Localization system. This can be called recursively.  
[LODUtility](LODUtility.html)| LOD Utility Helpers.  
[MainStage](SceneManagement.MainStage.html)| The Main Stage contains all the
currently open regular Scenes and is always available.  
[ManagedDebugger](Scripting.ManagedDebugger.html)| Representation of managed
debugger in UnityEditor.  
[MaskField](UIElements.MaskField.html)|  Make a field for masks.  
[MaterialDescription](AssetImporters.MaterialDescription.html)| Contains a set
of typed properties for describing a texture input of a MaterialDescription.  
[MaterialEditor](MaterialEditor.html)| The Unity Material Editor.  
[MaterialEditorExtensions](MaterialEditorExtensions.html)| Extension methods
for the Material asset type in the editor.  
[MaterialProperty](MaterialProperty.html)| Describes information and value of
a single shader property.  
[MaterialPropertyDrawer](MaterialPropertyDrawer.html)| Base class to derive
custom material property drawers from.  
[MaterialSettingsCallbackAttribute](SpeedTree.Importer.MaterialSettingsCallbackAttribute.html)|
This attribute is used as a callback to set SRP specific properties from the
importer.  
[MediaEncoder](Media.MediaEncoder.html)| Encodes images and audio samples into
an audio or movie file.  
[Menu](Menu.html)| Provides methods to manipulate a menu item.  
[MenuCommand](MenuCommand.html)| Used to extract the context for a MenuItem.  
[MenuItem](MenuItem.html)| The MenuItem attribute allows you to add menu items
to the main menu and Inspector window context menus.  
[MeshPreview](MeshPreview.html)| Use this class to render an interactive
preview of a mesh.  
[MeshUtility](MeshUtility.html)| Various utilities for mesh manipulation.  
[Message](VersionControl.Message.html)| Messages from the version control
system.  
[MiniMap](Experimental.GraphView.MiniMap.html)| MiniMap.  
[ModelImporter](ModelImporter.html)| Model importer lets you modify model
import settings from editor scripts.  
[ModelImporterClipAnimation](ModelImporterClipAnimation.html)| Animation clips
to split animation into.  
[MonoImporter](MonoImporter.html)| Represents a C# script in the project.  
[MonoScript](MonoScript.html)| Representation of Script assets.  
[MultiColumnHeader](IMGUI.Controls.MultiColumnHeader.html)| The
MultiColumnHeader is a general purpose class that e.g can be used with the
TreeView to create multi-column tree views and list views.  
[MultiColumnHeaderState](IMGUI.Controls.MultiColumnHeaderState.html)| State
used by the MultiColumnHeader.  
[NavMeshBuilder](AI.NavMeshBuilder.html)| Navigation mesh builder interface.  
[NavMeshEditorHelpers](AI.NavMeshEditorHelpers.html)| NavMesh utility
functionality effective only in the Editor.  
[NavMeshVisualizationSettings](AI.NavMeshVisualizationSettings.html)|
Represents the visualization state of the navigation debug graphics.  
[Node](Experimental.GraphView.Node.html)| Main GraphView node class.  
[ObjectChangeEvents](ObjectChangeEvents.html)| Exposes events that allow you
to track undoable changes to objects in the editor.  
[ObjectFactory](ObjectFactory.html)| Use the DefaultObject to create a new
UnityEngine.Object in the editor.  
[ObjectField](Search.ObjectField.html)| Object field used with the advanced
search picker.  
[ObjectField](UIElements.ObjectField.html)|  Makes a field to receive any
object type. For more information, refer to UXML element ObjectField.  
[ObjectIndexer](Search.ObjectIndexer.html)| A specialized SearchIndexer which
provides methods to index a Unity Object from custom indexers.  
[ObjectNames](ObjectNames.html)| Helper class for constructing displayable
names for objects.  
[ObjectOverride](SceneManagement.ObjectOverride.html)| Class with information
about an object on a Prefab instance with overridden properties.  
[ObjectPreview](ObjectPreview.html)| Base Class to derive from when creating
Custom Previews.  
[ObjectSelectorEngineAttribute](SearchService.ObjectSelectorEngineAttribute.html)|
Use this class attribute to register ObjectSelector search engines
automatically. Search engines with this attribute must implement the
IObjectSelectorEngine interface.  
[ObjectSelectorSearch](SearchService.ObjectSelectorSearch.html)| Use this API
to select objects. Engines for this type of search implement the
IObjectSelectorEngine interface.  
[ObjectSelectorSearchContext](SearchService.ObjectSelectorSearchContext.html)|
A search context implementation for ObjectSelector search engines. All methods
that are called on an ObjectSelector search engine, and expect a
ISearchContext, receive an object of this type.  
[OnInspectorGUIContext](TerrainTools.OnInspectorGUIContext.html)| The context
for drawing IMGUI elements pertaining to terrain tools brushes.  
[OnOpenAssetAttribute](Callbacks.OnOpenAssetAttribute.html)| Invokes a static
callback method when the Unity Editor attempts to open an asset.  
[Overlay](Overlays.Overlay.html)| Overlays are persistent and customizable
panels and toolbars that are available within Editor Windows. Use Overlays to
expose actions and tool options in a convenient and user-controllable way.  
[OverlayAttribute](Overlays.OverlayAttribute.html)| Attribute used to register
a class as an overlay.  
[OverlayCanvas](Overlays.OverlayCanvas.html)| OverlayCanvas is a container for
collections of Overlays.  
[OverlayToolbar](Overlays.OverlayToolbar.html)| Base class for toolbar
elements intended to be drawn in an Overlay.  
[PackageCollection](PackageManager.PackageCollection.html)| A collection of
PackageInfo objects that you can iterate over.  
[PackageInfo](PackageManager.PackageInfo.html)| Structure describing a Unity
Package.  
[PackageManagerExtensions](PackageManager.UI.PackageManagerExtensions.html)|
Package Manager UI Extensions.  
[PackageRegistrationEventArgs](PackageManager.PackageRegistrationEventArgs.html)|
Structure describing the PackageInfo entries to register or unregister during
the Package Manager registration process.  
[PackedAssets](Build.Reporting.PackedAssets.html)| An extension to the
BuildReport class that tracks how Assets contribute to the size of the build.  
[Packer](Sprites.Packer.html)| Sprite Packer helpers.  
[PackerJob](Sprites.PackerJob.html)| Current Sprite Packer job definition.  
[PackOperationResult](PackageManager.PackOperationResult.html)| Structure
describing the result of a Client.Pack operation.  
[PackRequest](PackageManager.Requests.PackRequest.html)| Represents an
asynchronous request to pack a package folder.  
[PaintDetailsToolUtility](TerrainTools.PaintDetailsToolUtility.html)| Provides
utility methods for painting details.  
[PaintTreesDetailsContext](TerrainTools.PaintTreesDetailsContext.html)|
Represents a context object for information used when scattering trees and
detail objects across terrains.  
[ParsedQuery<T0,T1>](Search.ParsedQuery_2.html)| Provides methods to define an
operation that can be used to filter a data set.  
[ParsedQuery<T0>](Search.ParsedQuery_1.html)| Provides methods to define an
operation that can be used to filter a data set.  
[PhysicsDebugWindow](PhysicsDebugWindow.html)| Displays the Physics Debug
Visualization options.The Physics Debug Visualization is only displayed if
this window is visible.Additional resources: PhysicsVisualizationSettings.  
[PhysicsVisualizationSettings](PhysicsVisualizationSettings.html)| This class
contains the settings controlling the Physics Debug Visualization.  
[Pill](Experimental.GraphView.Pill.html)| The Pill class includes methods for
creating and managing a VisualElement that resembles a capsule. The Pill class
includes text, an icon, and two optional child VisualElements: one to the left
of the pill, and one to the right of the pill.  
[Placemat](Experimental.GraphView.Placemat.html)| Allows interactive
manipulation of elements (drag, hide) over a virtual placemat.  
[PlacematContainer](Experimental.GraphView.PlacematContainer.html)| The
GraphView layer for placemats.  
[PlatformIcon](PlatformIcon.html)| Icon slot container.  
[PlatformIconKind](PlatformIconKind.html)| Icon kind wrapper.  
[PlayableOutputEditorExtensions](Playables.PlayableOutputEditorExtensions.html)|
Editor extensions for all types that implement IPlayableOutput.  
[PlayerBuildInterface](Build.Player.PlayerBuildInterface.html)| Low level
interface for building scripts for Unity.  
[PlayerConnectionGUI](Networking.PlayerConnection.PlayerConnectionGUI.html)|
This class contains methods to draw IMGUI Editor UI that relates to the Player
Connection.  
[PlayerConnectionGUILayout](Networking.PlayerConnection.PlayerConnectionGUILayout.html)|
This class contains methods to draw and automatically layout IMGUI Editor UI
that relates to the Player Connection.  
[PlayerConnectionGUIUtility](Networking.PlayerConnection.PlayerConnectionGUIUtility.html)|
Miscellaneous helper methods for PlayerConnectionGUI.  
[PlayerSettings](PlayerSettings.html)| Player Settings is where you define
various parameters for the final game that you will build in Unity. Some of
these values are used in the Resolution Dialog that launches when you open a
standalone game.  
[PlayModeWindow](PlayModeWindow.html)| Class containing methods to interact
with the selected Unity PlayModeView (GameView, Simulator).  
[Plugin](VersionControl.Plugin.html)| The plug-in class describes the
currently active version control plug-in and its configuration options.  
[PluginImporter](PluginImporter.html)| Represents a plugin importer.  
[PopupWindow](PopupWindow.html)| Class used to display popup windows that
inherit from PopupWindowContent.  
[PopupWindowContent](PopupWindowContent.html)| Class used to implement content
for a popup window.  
[Port](Experimental.GraphView.Port.html)| GraphView Port class.  
[PortSource<T0>](Experimental.GraphView.PortSource_1.html)| Port source.  
[PostProcessBuildAttribute](Callbacks.PostProcessBuildAttribute.html)| Add
this attribute to a method to get a notification just after building the
player.  
[PostProcessSceneAttribute](Callbacks.PostProcessSceneAttribute.html)| Add
this attribute to a method to get a notification just after building the
Scene.  
[PrefabOverride](SceneManagement.PrefabOverride.html)| Class with information
about a given override on a Prefab instance.  
[PrefabReplacingSettings](PrefabReplacingSettings.html)| Settings controlling
the behavior of PrefabUtility.ReplacePrefabAssetOfPrefabInstance.  
[PrefabStage](SceneManagement.PrefabStage.html)| The PrefabStage class
represents an editing context for Prefab Assets.  
[PrefabStageUtility](SceneManagement.PrefabStageUtility.html)| Utility methods
related to Prefab stages.  
[PrefabUtility](PrefabUtility.html)| Utility class for any Prefab related
operations.  
[PreloadInfo](Build.Content.PreloadInfo.html)| Container for holding a list of
preload objects for a Scene to be built.  
[Preset](Presets.Preset.html)| A Preset contains default values for an Object.  
[PresetSelector](Presets.PresetSelector.html)| This class implements a modal
window that selects a Preset asset from the Project.  
[PreviewSceneStage](SceneManagement.PreviewSceneStage.html)| The
PreviewSceneStage class represents an editing context based on a single
preview Scene.  
[PrimitiveBoundsHandle](IMGUI.Controls.PrimitiveBoundsHandle.html)| Base class
for a compound handle to edit a bounding volume in the Scene view.  
[ProcessService](MPE.ProcessService.html)| *This is an experimental feature.*
The ProcessService allows you to start slave instance of UnityEditor, opened
to the same Project as the master instance, with a specific
RoleProviderAttribute.  
[ProfilerEditorUtility](Profiling.ProfilerEditorUtility.html)| A Utility class
for Profiler tooling in the Unity Editor.  
[ProfilerModule](Unity.Profiling.Editor.ProfilerModule.html)| Represents a
Profiler module in the Profiler window.  
[ProfilerModuleMetadataAttribute](Unity.Profiling.Editor.ProfilerModuleMetadataAttribute.html)|
Provides metadata related to a ProfilerModule, such as its name and icon path.  
[ProfilerModuleViewController](Unity.Profiling.Editor.ProfilerModuleViewController.html)|
Provides a single view of content for a ProfilerModule displayed in the
Profiler window.  
[ProfilerTimeSampleSelection](Profiling.ProfilerTimeSampleSelection.html)| An
object describing a selection made in a frame time sample based Profiler
module.  
[ProfilerWindow](ProfilerWindow.html)| Use the ProfilerWindow class for
interactions with the Profiler Window such as checking which frame it
currently shows and controlling the selected Profiler sample in the CPU or GPU
Usage Modules.  
[Progress](Progress.html)| The Progress utility class reports the progress of
asynchronous tasks to Unity.  
[ProjectBindDrawer](Connect.ProjectBindDrawer.html)| A container that fetches
the UIElements that draw the Project Binding UI, and subscribes to its events.  
[ProjectSearch](SearchService.ProjectSearch.html)| Use this API to perform
searches in the Project. Engines for this type of search implement the
IProjectSearchEngine interface.  
[ProjectSearchContext](SearchService.ProjectSearchContext.html)| A search
context implementation for Project search engines. All methods that are called
on a Project search engine, and expect a ISearchContext, receive an object of
this type.  
[ProjectSearchEngineAttribute](SearchService.ProjectSearchEngineAttribute.html)|
A class attribute that registers Project search engines automatically. Search
engines with this attribute must implement the IProjectSearchEngine interface.  
[PropertyDatabase](Search.PropertyDatabase.html)| The PropertyDatabase is a
system that can store, in a thread-safe manner, properties of different kinds
into a single file that we call a property database.  
[PropertyDrawer](PropertyDrawer.html)| Base class to derive custom property
drawers from. Use this to create custom drawers for your own Serializable
classes or for script variables with custom PropertyAttributes.  
[PropertyField](UIElements.PropertyField.html)|  A SerializedProperty wrapper
VisualElement that, on Bind(), will generate the correct field elements with
the correct binding paths. For more information, refer to UXML element
PropertyField.  
[PropertyModification](PropertyModification.html)| Defines a single modified
property.  
[Provider](VersionControl.Provider.html)| This class provides access to the
version control API.  
[PurchasingSettings](Purchasing.PurchasingSettings.html)| Editor API for the
Unity Services editor feature. Normally Purchasing is enabled from the
Services window, but if writing your own editor extension, this API can be
used.  
[QueryBlock](Search.QueryBlock.html)| A query block is the visual element of a
query node in a query.  
[QueryEngine](Search.QueryEngine.html)| A QueryEngine defines how to build a
query from an input string. It can be customized to support custom filters and
operators. Default query engine of type object.  
[QueryEngine<T0>](Search.QueryEngine_1.html)| A QueryEngine defines how to
build a query from an input string. It can be customized to support custom
filters and operators.  
[QueryEngineFilterAttribute](Search.QueryEngineFilterAttribute.html)| Base
attribute class used to define a custom filter on a QueryEngine. All filter
types supported by QueryEngine.AddFilter are supported by this attribute.  
[QueryEngineParameterTransformerAttribute](Search.QueryEngineParameterTransformerAttribute.html)|
Base attribute class that defines a custom parameter transformer function.  
[QueryError](Search.QueryError.html)| A QueryError holds the definition of a
query parsing error.  
[QueryGraph](Search.QueryGraph.html)| Class that represents a query graph.  
[QueryListBlock](Search.QueryListBlock.html)| A query list block represents a
special query block that will list a set of value for a given filter.  
[QueryListBlockAttribute](Search.QueryListBlockAttribute.html)| This attribute
can be used on a class deriving from QueryListBlock to display in query
builder mode a special block that will propose a fixed set of values when
clicked.  
[RadeonRaysContext](LightTransport.RadeonRaysContext.html)|  RadeonRaysContext
implements the IDeviceContext interface. It uses the RadeonRays SDK for
intersection testing and the OpenCL 1.2 API for compute.  
[RadeonRaysProbeIntegrator](LightTransport.RadeonRaysProbeIntegrator.html)|
RadeonRays-based light probe integrator.  
[RadeonRaysProbePostProcessor](LightTransport.PostProcessing.RadeonRaysProbePostProcessor.html)|
RadeonRaysProbePostProcessor.  
[RadeonRaysWorld](LightTransport.RadeonRaysWorld.html)| RadeonRays integration
world.  
[RawFrameDataView](Profiling.RawFrameDataView.html)| Provides access to the
Profiler data for a specific frame and thread.  
[RectangleSelector](Experimental.GraphView.RectangleSelector.html)| Rectangle
selection box manipulator.  
[RectUtils](Experimental.GraphView.RectUtils.html)| Utilities for rectangle
selections.  
[ReferenceContext](LightTransport.ReferenceContext.html)| The ReferenceContext
implements the IDeviceContext interface.  
[ReferenceProbePostProcessor](LightTransport.PostProcessing.ReferenceProbePostProcessor.html)|
The ReferenceProbePostProcessor implements the IProbePostProcessor interface.  
[RegistryInfo](PackageManager.RegistryInfo.html)| Provides information about a
package registry.  
[RemovedComponent](SceneManagement.RemovedComponent.html)| Class with
information about a component that has been removed from a Prefab instance.  
[RemovedGameObject](SceneManagement.RemovedGameObject.html)| Class with
information about a GameObject that has been removed from a Prefab instance.  
[RemoveIfAttribute](ShaderKeywordFilter.RemoveIfAttribute.html)| Remove the
specified shader keywords from the build if the data field matches the
condition.  
[RemoveIfNotAttribute](ShaderKeywordFilter.RemoveIfNotAttribute.html)| Remove
the specified shader keywords from the build if the data field doesn't match
the condition.  
[RemoveOrSelectAttribute](ShaderKeywordFilter.RemoveOrSelectAttribute.html)|
Either remove or include the specified shader keywords in the build, depending
on the data field underneath.  
[RemoveRequest](PackageManager.Requests.RemoveRequest.html)| Represents an
asynchronous request to remove a package from the project.  
[RenderingLayerMaskField](UIElements.RenderingLayerMaskField.html)| Drawer for
RenderingLayerMask.  
[RenderingLayersLimitSettings](Rendering.RenderingLayersLimitSettings.html)|
Define a number of supported Rendering Layers on the Render Pipeline.  
[RenderPipelineEditorUtility](Rendering.RenderPipelineEditorUtility.html)|
Helper class that contains a utility function on ScriptableRenderPipeline for
Editor.  
[RenderPipelineGraphicsSettingsEditorUtility](Rendering.RenderPipelineGraphicsSettingsEditorUtility.html)|
Helper class that contains a utility function on
IRenderPipelineGraphicsSettings for Editor.  
[RepositoryInfo](PackageManager.RepositoryInfo.html)| Includes information
about the repository that hosts the package.  
[Request](PackageManager.Requests.Request.html)| Tracks the state of an
asynchronous Unity Package Manager (Upm) server operation.  
[Request<T0>](PackageManager.Requests.Request_1.html)| Tracks the state of an
asynchronous Unity Package Manager (Upm) server operation that returns a non-
empty response.  
[ReserveModifiersAttribute](ShortcutManagement.ReserveModifiersAttribute.html)|
Provides an attribute that reserves one or multiple modifiers for a specific
shortcut.  
[ResetToEditorDefaultsRequest](PackageManager.Requests.ResetToEditorDefaultsRequest.html)|
Represents an asynchronous request to reset the project packages to the
current Editor default configuration.  
[ResizableElement](Experimental.GraphView.ResizableElement.html)| Instantiates
a [ResizableElement] that you add as a child of the [VisualElement] that you
want to resize.  
[Resizer](Experimental.GraphView.Resizer.html)| Resizer manipulator element.  
[ResponseFileData](Compilation.ResponseFileData.html)| Data class used for
storing parsed response file data.  
[RoleProviderAttribute](MPE.RoleProviderAttribute.html)| An attribute used to
decorate function that defines how a slave process can interact with a main
instance of Unity.  
[RunAfterAssemblyAttribute](Callbacks.RunAfterAssemblyAttribute.html)| Add
this attribute to a callback method to mark that this callback must be run
after any callbacks that are part of the specified assembly.  
[RunAfterClassAttribute](Callbacks.RunAfterClassAttribute.html)| Add this
attribute to a callback method to mark that this callback must be run after
any callbacks that are part of the specified class.  
[RunAfterPackageAttribute](Callbacks.RunAfterPackageAttribute.html)| Add this
attribute to a callback method to mark that this callback must be run after
any callbacks that are part of the specified package.  
[RunBeforeAssemblyAttribute](Callbacks.RunBeforeAssemblyAttribute.html)| Add
this attribute to a callback method to indicate that this callback must be run
before any callbacks that are part of the specified assembly.  
[RunBeforeClassAttribute](Callbacks.RunBeforeClassAttribute.html)| Add this
attribute to a callback method to mark that this callback must be run before
any callbacks that are part of the specified class.  
[RunBeforePackageAttribute](Callbacks.RunBeforePackageAttribute.html)| Add
this attribute to a callback method to mark that this callback must be run
before any callbacks that are part of the specified package.  
[SaveData](Overlays.SaveData.html)| A serializable storage for the state of an
Overlay.  
[SceneAsset](SceneAsset.html)| SceneAsset is used to reference Scene objects
in the Editor.  
[SceneBundleInfo](Build.Content.SceneBundleInfo.html)| Container for holding
asset loading information for a streamed Scene AssetBundle to be built.  
[SceneCullingMasks](SceneManagement.SceneCullingMasks.html)| Masks that
control what kind of Scene views and Game views Unity should render a
GameObject in.  
[SceneLoadInfo](Build.Content.SceneLoadInfo.html)| Container for holding
preload information for a given serialized Scene in an AssetBundle.  
[SceneQueryEngineFilterAttribute](Search.Providers.SceneQueryEngineFilterAttribute.html)|
Custom attribute is used to customize the search engine used by the scene
search provider.  
[SceneQueryEngineParameterTransformerAttribute](Search.Providers.SceneQueryEngineParameterTransformerAttribute.html)|
Attribute class that defines a custom parameter transformer function applied
for a query running in a scene provider defined by a scene custom filter using
SceneQueryEngineFilterAttribute.  
[SceneSearch](SearchService.SceneSearch.html)| Use this API to perform
searches in the Scene. Engines for this type of search implement the
ISceneSearchEngine interface.  
[SceneSearchContext](SearchService.SceneSearchContext.html)| A search context
implementation for Scene search engines. All methods that are called on a
Scene search engine, and expect a ISearchContext, receive an object of this
type.  
[SceneSearchEngineAttribute](SearchService.SceneSearchEngineAttribute.html)| A
class attribute that registers Scene search engines automatically. Search
engines with this attribute must implement the ISceneSearchEngine interface.  
[SceneSetup](SceneManagement.SceneSetup.html)| The setup information for a
Scene in the SceneManager. This cannot be used in Play Mode.  
[ScenesUsingAssets](Build.Reporting.ScenesUsingAssets.html)| An extension to
the BuildReport class that tracks which scenes in the build have references to
a specific asset in the build.  
[SceneTemplateAsset](SceneTemplate.SceneTemplateAsset.html)| An Asset that
stores everything required to instantiate a new Scene from a templated Scene.  
[SceneTemplatePipelineAdapter](SceneTemplate.SceneTemplatePipelineAdapter.html)|
An adapter that implements all the functions of ISceneTemplatePipeline for
easier usage. Use it to partially override a ISceneTemplatePipeline.  
[SceneTemplateService](SceneTemplate.SceneTemplateService.html)| A utility
class that manages SceneTemplateAsset instantiation.  
[SceneView](SceneView.html)| Use this class to manage SceneView settings,
change the SceneView camera properties, subscribe to events, call SceneView
methods, and render open scenes.  
[SceneViewCameraWindow](SceneViewCameraWindow.html)| Use this class to
instantiate a SceneViewCameraWindow window.  
[SceneVisibilityManager](SceneVisibilityManager.html)| Manages Scene
Visibility in the editor.  
[Scope](Experimental.GraphView.Scope.html)| This class allows for nodes to be
grouped into a common area, or Scope. This class includes methods that
automatically resize and position the Scope to encompass the group of nodes.  
[ScriptableBakedReflectionSystem](Experimental.Rendering.ScriptableBakedReflectionSystem.html)|
Empty implementation of IScriptableBakedReflectionSystem.  
[ScriptableBakedReflectionSystemSettings](Experimental.Rendering.ScriptableBakedReflectionSystemSettings.html)|
Global settings for the scriptable baked reflection system.  
[ScriptablePacker](U2D.ScriptablePacker.html)| ScriptablePacker Interface.
Provides a custom implementation to pack sprites into textures. This is the
Scriptable Packer interface.  
[ScriptableSingleton<T0>](ScriptableSingleton_1.html)| Generic class for
storing Editor state.  
[ScriptableWizard](ScriptableWizard.html)| Derive from this class to create an
editor wizard.  
[ScriptCompilerOptions](Compilation.ScriptCompilerOptions.html)| Compiler
options passed to the script compiler.  
[ScriptedImporter](AssetImporters.ScriptedImporter.html)| Abstract base class
for custom Asset importers.  
[ScriptedImporterAttribute](AssetImporters.ScriptedImporterAttribute.html)|
Class attribute used to register a custom asset importer derived from
ScriptedImporter with Unity's Asset import pipeline.  
[ScriptedImporterEditor](AssetImporters.ScriptedImporterEditor.html)| Default
editor for source assets handled by Scripted Importers.  
[SearchAction](Search.SearchAction.html)| Defines an action that can be
applied on a SearchItem of a specific search provider type.  
[SearchActionsProviderAttribute](Search.SearchActionsProviderAttribute.html)|
Attribute used to declare a static method that defines new actions for
specific search providers.  
[SearchColumn](Search.SearchColumn.html)| Search columns are used to display
additional information in the Search Table view.  
[SearchColumnProviderAttribute](Search.SearchColumnProviderAttribute.html)|
The search column provider attribute is used to define new formats for a given
column.  
[SearchContext](Search.SearchContext.html)| The search context includes all
the data necessary to perform a query. It allows the full customization of how
a query may be performed.  
[SearchExpression](Search.SearchExpression.html)| Search expressions allow you
to add to the search query language to express complex queries that cross-
reference multiple providers, for example, to search for all objects in a
scene that use a shader that doesn’t compile.Search expressions can be chained
together to transform or perform set manipulations on Search Items.The manual
contains example on How to use Search Expression .  
[SearchExpressionEvaluatorAttribute](Search.SearchExpressionEvaluatorAttribute.html)|
Attribute used to register new SearchExpressionEvaluator. This will allow to
use new function in SearchExpression. As a side note all builtin evaluators
(count{}, select{}, ...) are defined using this attribute.  
[SearchExpressionEvaluatorSignatureOverloadAttribute](Search.SearchExpressionEvaluatorSignatureOverloadAttribute.html)|
Allows user to add more function signature overload to a
SearchExpressionEvaluatorAttribute.  
[SearchField](IMGUI.Controls.SearchField.html)| The SearchField control
creates a text field for a user to input text that can be used for searching.  
[SearchFieldBase<T0,T1>](UIElements.SearchFieldBase_2.html)|  The base class
for a search field.  
[SearchIndexer](Search.SearchIndexer.html)| Base class for a document Indexer
which provides methods for retrieving a document given a specific pattern in
roughly log(n). This allows you to search a large index more quickly.  
[SearchItem](Search.SearchItem.html)| Search items are returned by the search
provider to show to the user after a search is performed. The search item
holds all the data that is used to sort and present the search results. Some
members of a SearchItem can be specified in an asynchronous callback (see
SearchItem.fetchThumbnail, SearchItem.fetchDescription, etc).  
[SearchItemProviderAttribute](Search.SearchItemProviderAttribute.html)|
Attribute used to declare a static method that will create a new search
provider at load time.  
[SearchMonitor](Search.SearchMonitor.html)| The search monitor is responsible
to track any changes that occurs in Unity in order to update search indexes or
other search data structure at runtime.  
[SearchPropositionFlagsExtensions](Search.SearchPropositionFlagsExtensions.html)|
Search proposition flags extension used to manipulate flag bits.  
[SearchPropositionOptions](Search.SearchPropositionOptions.html)| Search
proposition options are used define how search propositions are fetched and
displayed.  
[SearchProvider](Search.SearchProvider.html)| SearchProvider manages search
for specific types of items and manages all fields of a SearchItem such as
thumbnails, descriptions, subfilters.  
[SearchQueryError](Search.SearchQueryError.html)| Represents a query parsing
error.  
[SearchRequest](PackageManager.Requests.SearchRequest.html)| Represents an
asynchronous request to find a package.  
[SearchSelection](Search.SearchSelection.html)| Provides methods to give
readonly access to the current list of selected items in Search.  
[SearchSelectorAttribute](Search.SearchSelectorAttribute.html)| Search
selector attribute used to define how a custom value can be selected from a
search item.  
[SearchService](Search.SearchService.html)| Principal Search API to initiate
searches and fetch results.  
[SearchSettings](Search.SearchSettings.html)| Search settings give access to
the user global preferences regarding Search.  
[SearchTable](Search.SearchTable.html)| A search table configuration is used
to define the columns when search results are displayed in table view.  
[SearchTreeEntry](Experimental.GraphView.SearchTreeEntry.html)| This class
describes a search tree entry. The search window displays search tree entries
in the GraphView.  
[SearchTreeGroupEntry](Experimental.GraphView.SearchTreeGroupEntry.html)| This
class describes group entries in the search tree. The search tree is displayed
in the search window.  
[SearchUtils](Search.SearchUtils.html)| Provides various utility functions
that are used by SearchProvider.  
[SearchViewState](Search.SearchViewState.html)| Search view state is used to
create new Search windows. See SearchService.ShowWindow.  
[SearchWindow](Experimental.GraphView.SearchWindow.html)| This subclass
displays a searchable menu of available graph nodes.  
[SelectIfAttribute](ShaderKeywordFilter.SelectIfAttribute.html)| Include only
the specified shader keywords in the build if the data field matches the
condition.  
[SelectIfNotAttribute](ShaderKeywordFilter.SelectIfNotAttribute.html)| Include
only the specified shader keywords in the build if the data field doesn't
match the condition.  
[Selection](Selection.html)| Access to the selection in the editor.  
[SelectionDragger](Experimental.GraphView.SelectionDragger.html)| Selection
dragger manipulator.  
[SelectionDropper](Experimental.GraphView.SelectionDropper.html)| Selection
drag&drop manipulator.  
[SelectOrRemoveAttribute](ShaderKeywordFilter.SelectOrRemoveAttribute.html)|
Either include or remove the specified shader keywords in the build, depending
on the data field underneath.  
[SerializationInfo](Build.Content.SerializationInfo.html)| Container for
holding object serialization order information for a build.  
[SerializationUtility](SerializationUtility.html)| Utility functions related
to Serialization.  
[SerializedObject](SerializedObject.html)| SerializedObject and
SerializedProperty are classes for editing serialized fields on Unity objects
in a completely generic way. These classes automatically handle dirtying
individual serialized fields so they will be processed by the Undo system and
styled correctly for Prefab overrides when drawn in the Inspector.  
[SerializedObjectChangeEvent](UIElements.SerializedObjectChangeEvent.html)|
An event sent when any value in a SerializedObject changes  
[SerializedProperty](SerializedProperty.html)| SerializedProperty and
SerializedObject are classes for editing properties on objects in a completely
generic way that automatically handles undo, multi-object editing and Prefab
overrides.  
[SerializedPropertyChangeEvent](UIElements.SerializedPropertyChangeEvent.html)|
An event sent when a value in a PropertyField changes.  
[SessionState](SessionState.html)| SessionState is a Key-Value Store intended
for storing and retrieving Editor session state that should survive assembly
reloading.  
[SettingsProvider](SettingsProvider.html)| SettingsProvider is the
configuration class that specifies how a Project setting or a preference
should appear in the Settings or Preferences window.  
[SettingsProviderAttribute](SettingsProviderAttribute.html)| Attribute used to
register a new SettingsProvider. Use this attribute to decorate a function
that returns an instance of a SettingsProvider. If the function returns null,
no SettingsProvider appears in the Settings window.  
[SettingsProviderGroupAttribute](SettingsProviderGroupAttribute.html)|
Attribute used to register multiple SettingsProvider items. Use this attribute
to decorate a function that returns an array of SettingsProvider instances. If
the function returns null, no SettingsProvider appears in the Settings window.  
[SettingsService](SettingsService.html)| This class provides global APIs to
interact with the Settings window.  
[ShaderData](ShaderData.html)| This class describes a shader.  
[ShaderGUI](ShaderGUI.html)| Abstract class to derive from for defining custom
GUI for shader properties and for extending the material preview.  
[ShaderImporter](ShaderImporter.html)| Shader importer lets you modify shader
import settings from Editor scripts.  
[ShaderInclude](ShaderInclude.html)| Shader include file asset.  
[ShaderUtil](ShaderUtil.html)| Utility functions to assist with working with
shaders from the editor.  
[ShortcutAttribute](ShortcutManagement.ShortcutAttribute.html)| Registers a
static method as the action for an action shortcut.  
[ShortcutBaseAttribute](ShortcutManagement.ShortcutBaseAttribute.html)|
Abstract base class for ShortcutAttribute and ClutchShortcutAttribute.  
[ShortcutHandler](Experimental.GraphView.ShortcutHandler.html)| Shortcut
handler.  
[ShortcutManager](ShortcutManagement.ShortcutManager.html)| Provides access to
an instance of IShortcutManager for managing shortcuts.  
[SketchUpImporter](SketchUpImporter.html)| Derives from AssetImporter to
handle importing of SketchUp files.  
[SketchupMaterialDescriptionPreprocessor](AssetImporters.SketchupMaterialDescriptionPreprocessor.html)|
This is a default implementation for
AssetPostProcessor.OnPreprocessMaterialDescription, this implementation
converts material descriptions imported from Sketchup assets into materials
for the internal rendering pipeline.  
[SourceTextureInformation](AssetImporters.SourceTextureInformation.html)|
Original texture data information.  
[SpeedTree9Importer](SpeedTree.Importer.SpeedTree9Importer.html)| Represents
the SpeedTree 9 asset importer, providing methods for processing and post-
processing SpeedTree assets during import.  
[SpeedTreeImporter](SpeedTreeImporter.html)| AssetImporter for importing
SpeedTree model assets.  
[SphereBoundsHandle](IMGUI.Controls.SphereBoundsHandle.html)| A compound
handle to edit a sphere-shaped bounding volume in the Scene view.  
[SpriteAtlasAsset](U2D.SpriteAtlasAsset.html)| SpriteAtlasAsset stores inputs
for generating SpriteAtlas and generates atlas textures on Import.  
[SpriteAtlasExtensions](U2D.SpriteAtlasExtensions.html)| Method extensions for
SpriteAtlas in Editor.  
[SpriteAtlasImporter](U2D.SpriteAtlasImporter.html)| SpriteAtlasImporter
imports SpriteAtlasAsset and generates SpriteAtlas.  
[SpriteAtlasUtility](U2D.SpriteAtlasUtility.html)| Utility methods to pack
atlases in the Project.  
[SpriteEditorExtension](U2D.SpriteEditorExtension.html)|  Sprite extension
methods that are accessible in Editor only.  
[SpriteUtility](Sprites.SpriteUtility.html)| Helper utilities for accessing
Sprite data.  
[StackNode](Experimental.GraphView.StackNode.html)| Use this class to
customize StackNodes and to manage dragging GraphElements over StackNodes.  
[Stage](SceneManagement.Stage.html)| The Stage class represents an editing
context which includes a collection of Scenes.  
[StageUtility](SceneManagement.StageUtility.html)| Utility methods related to
stages.  
[StateMachineBehaviourContext](Animations.StateMachineBehaviourContext.html)|
This class contains all the owner's information for this State Machine
Behaviour.  
[StaticOcclusionCulling](StaticOcclusionCulling.html)| StaticOcclusionCulling
lets you perform static occlusion culling operations.  
[StaticOcclusionCullingVisualization](StaticOcclusionCullingVisualization.html)|
Used to visualize static occlusion culling at development time in Scene view.  
[StickyNote](Experimental.GraphView.StickyNote.html)| Instantiates a
[GraphElement] used for comment text.  
[StickyNoteChangeEvent](Experimental.GraphView.StickyNoteChangeEvent.html)|
The event sent when a [StickyNote] was changed.  
[StrippingInfo](Build.Reporting.StrippingInfo.html)| The StrippingInfo object
contains information about which native code modules in the engine are still
present in the build, and the reasons why they are still present.  
[Sysroot](Sysroot.html)| Base class for implementing sysroots and toolchains
for IL2CPP  
[TagConstraintAttribute](ShaderKeywordFilter.TagConstraintAttribute.html)|
Enable or disable shader keyword filter attributes based on shader tags.  
[TagField](UIElements.TagField.html)|  A TagField editor. For more
information, refer to UXML element TagField.  
[Task](VersionControl.Task.html)| A Task describes an instance of a version
control operation.  
[TerrainDetailMeshWizard](TerrainDetailMeshWizard.html)| Provides methods for
displaying the detail mesh wizard.  
[TerrainDetailTextureWizard](TerrainDetailTextureWizard.html)| Provides
methods for displaying the detail texture wizard.  
[TerrainInspectorUtility](TerrainTools.TerrainInspectorUtility.html)| Utility
class for Terrain Inspector GUI.  
[TerrainLayerInspector](TerrainLayerInspector.html)| The default Inspector
class for Terrain Layer.  
[TerrainLayerUtility](TerrainLayerUtility.html)| A set of helper functions for
using terrain layers.  
[TerrainPaintTool<T0>](TerrainTools.TerrainPaintTool_1.html)| Base class for
terrain painting tools.  
[TerrainPaintToolWithOverlays<T0>](TerrainTools.TerrainPaintToolWithOverlays_1.html)|
Base class for Terrain painting tools, which inherit from Editor Tools.  
[TerrainPaintToolWithOverlaysBase](TerrainTools.TerrainPaintToolWithOverlaysBase.html)|
The abstract class that TerrainPaintToolWithOverlays inherits from.  
[TerrainPaintUtilityEditor](TerrainTools.TerrainPaintUtilityEditor.html)|
Terrain paint utility editor helper functions.  
[TerrainToolShortcutContext](TerrainTools.TerrainToolShortcutContext.html)|
The shortcut context that is active while editing Terrain.  
[TerrainWizard](TerrainWizard.html)| Provides methods for displaying the
terrain wizard.  
[TextureGenerator](AssetImporters.TextureGenerator.html)| Experimental
utilities for generating Texture2D.  
[TextureImporter](TextureImporter.html)| Texture importer lets you modify
Texture2D import settings from editor scripts.  
[TextureImporterPlatformSettings](TextureImporterPlatformSettings.html)|
Stores platform specifics settings of a TextureImporter.  
[TextureImporterSettings](TextureImporterSettings.html)| Stores settings of a
TextureImporter.  
[ThreeDSMaterialDescriptionPreprocessor](AssetImporters.ThreeDSMaterialDescriptionPreprocessor.html)|
This is a default implementation for
AssetPostProcessor.OnPreprocessMaterialDescription, this implementation
converts material descriptions imported from .3DS assets into materials for
the internal rendering pipeline.  
[TileBaseEditor](TileBaseEditor.html)| Default editor for TileBase assets.  
[TileEditor](TileEditor.html)| Default editor for Tile assets.  
[TokenNode](Experimental.GraphView.TokenNode.html)| The TokenNode class
includes methods for creating and managing a Node that resembles a capsule.
The TokenNode class includes a title, an icon, one input Port, and one output
Port.  
[ToolAttribute](EditorTools.ToolAttribute.html)| Base class from which
EditorToolAttribute and EditorToolContextAttribute inherit.  
[Toolbar](UIElements.Toolbar.html)|  A toolbar for tool windows. For more
information, refer to UXML element Toolbar.  
[ToolbarBreadcrumbs](UIElements.ToolbarBreadcrumbs.html)|  Creates a
breadcrumb UI element for the toolbar to help users navigate a hierarchy. For
example, the visual scripting breadcrumb toolbar makes it easier to explore
scripts because users can jump to any level of the script by clicking a
breadcrumb item. For more information, refer to UXML element
ToolbarBreadcrumbs.  
[ToolbarButton](UIElements.ToolbarButton.html)|  A button for the toolbar. For
more information, refer to UXML element ToolbarButton.  
[ToolbarMenu](UIElements.ToolbarMenu.html)|  A drop-down menu for the toolbar.
For more information, refer to UXML element ToolbarMenu.  
[ToolbarMenuElementExtensions](UIElements.ToolbarMenuElementExtensions.html)|
An extension class that handles menu management for elements that are
implemented with the IToolbarMenuElement interface, but are identical to
DropdownMenu.  
[ToolbarOverlay](Overlays.ToolbarOverlay.html)|  ToolbarOverlay is an
implementation of Overlay that provides a base for Overlays that can be placed
in horizontal or vertical toolbars.  
[ToolbarPopupSearchField](UIElements.ToolbarPopupSearchField.html)|  The pop-
up search field for the toolbar. The search field includes a menu button. For
more information, refer to UXML element ToolbarPopupSearchField.  
[ToolbarSearchField](UIElements.ToolbarSearchField.html)|  A search field for
the toolbar. For more information, refer to UXML element ToolbarSearchField.  
[ToolbarSpacer](UIElements.ToolbarSpacer.html)|  A toolbar spacer of static
size. For more information, refer to UXML element ToolbarSpacer.  
[ToolbarToggle](UIElements.ToolbarToggle.html)|  A toggle for the toolbar. For
more information, refer to UXML element ToolbarToggle.  
[ToolManager](EditorTools.ToolManager.html)| This class manipulates editor
tools in the Scene view.  
[Tools](Tools.html)| Class used to manipulate the tools used in Unity's Scene
View.  
[TransformUtils](TransformUtils.html)| Editor Transform Utility Class.  
[TreeView](IMGUI.Controls.TreeView.html)| The TreeView is an IMGUI control
that lets you create tree views, list views and multi-column tables for Editor
tools.  
[TreeViewItem](IMGUI.Controls.TreeViewItem.html)| The TreeViewItem is used to
build the tree representation of a tree data structure.  
[TreeViewState](IMGUI.Controls.TreeViewState.html)| The TreeViewState contains
serializable state information for the TreeView.  
[TrueTypeFontImporter](TrueTypeFontImporter.html)| AssetImporter for importing
Fonts.  
[TypeCache](TypeCache.html)| Provides methods for fast type extraction from
assemblies loaded into the Unity Domain.  
[TypeDB](Build.Player.TypeDB.html)| Container for holding information about
script type and property data.  
[Undo](Undo.html)| Lets you register undo operations on specific objects you
are about to perform changes on.  
[UnityEventTools](Events.UnityEventTools.html)| Editor tools for working with
persistent UnityEvents.  
[UnityLinkerBuildPipelineData](UnityLinker.UnityLinkerBuildPipelineData.html)|
Contains information for various IUnityLinkerProcessor callbacks.  
[Unwrapping](Unwrapping.html)| Utility class for computing mesh UVs.  
[Utility](Playables.Utility.html)| Editor utility functions for the Playable
graph and its nodes.  
[UxmlAttributeConverter<T0>](UIElements.UxmlAttributeConverter_1.html)|
Converts a UxmlAttribute type to and from a string.  
[UxmlNamespacePrefixAttribute](UIElements.UxmlNamespacePrefixAttribute.html)|
Attribute that can be used on an assembly to define an XML namespace prefix
for a namespace.  
[UxmlSerializedDataCreator](UIElements.UxmlSerializedDataCreator.html)|
Editor utility methods for dealing with UxmlSerializedData.  
[VersionControlAttribute](VersionControl.VersionControlAttribute.html)| Allows
you to mark a class as a version control system object.  
[VersionControlDescriptor](VersionControl.VersionControlDescriptor.html)|
Contains unique version control system name.  
[VersionControlManager](VersionControl.VersionControlManager.html)| Manages
version control systems.  
[VersionControlObject](VersionControl.VersionControlObject.html)| The abstract
base class for representing a version control system.  
[VersionControlUtils](VersionControl.VersionControlUtils.html)| Contains
version control system specific utility methods.  
[VersionsInfo](PackageManager.VersionsInfo.html)| Identifies the available
versions of a package and which are the compatible, latest, and recommended
versions.  
[VideoClipImporter](VideoClipImporter.html)| VideoClipImporter lets you modify
VideoClip import settings from Editor scripts.  
[VideoImporterTargetSettings](VideoImporterTargetSettings.html)| Importer
settings that can have platform-specific values.  
[Viewpoint<T0>](Viewpoint_1.html)| Defines a Viewpoint that can be selected
from the Cameras overlay.  
[WriteCommand](Build.Content.WriteCommand.html)| Container for holding
information about a serialized file to be written.  
  
### Structs

[ActiveProfileChangedEventArgs](ShortcutManagement.ActiveProfileChangedEventArgs.html)|
Provides data for the IShortcutManager.activeProfileChanged event.  
---|---  
[AdvancedObjectSelectorParameters](SearchService.AdvancedObjectSelectorParameters.html)|
Struct containing the different parameters passed to the advanced object
selector.  
[AlbedoSwatchInfo](Rendering.AlbedoSwatchInfo.html)| Contains the custom
albedo swatch data.  
[AndroidDeviceFilterData](AndroidDeviceFilterData.html)| Set of parameters
used to define an Android device or group of Android devices.  
[AnimatorCondition](Animations.AnimatorCondition.html)| Condition that is used
to determine if a transition must be taken.  
[ArtifactID](Experimental.ArtifactID.html)| Uniquely identifies a produced
artifact such as an imported asset (e.g. result of importing a texture).  
[ArtifactKey](Experimental.ArtifactKey.html)| An ArtifactKey is used for
specifying an artifact to lookup or produce.  
[AssemblyDefinitionPlatform](Compilation.AssemblyDefinitionPlatform.html)|
Contains information about a platform supported by the assembly definition
files.  
[AssetBundleBuild](AssetBundleBuild.html)| AssetBundle building map entry.  
[AssetIndexChangeSet](Search.AssetIndexChangeSet.html)| Defines a set of
changes that happens in order to update a search asset index.  
[AtlasSettings](Sprites.AtlasSettings.html)| Describes the final atlas
texture.  
[AudioImporterSampleSettings](AudioImporterSampleSettings.html)| This
structure contains a collection of settings used to define how an AudioClip
should be imported.This structure is used with the AudioImporter to define how
the AudioClip should be imported and treated during loading within the Scene.  
[AudioTrackAttributes](Media.AudioTrackAttributes.html)| Descriptor for audio
track format.  
[BufferID](LightTransport.BufferID.html)| Abstraction layer for memory
buffers.  
[BufferSlice<T0>](LightTransport.BufferSlice_1.html)| Unity uses the
BufferSlice struct to split one large buffer allocation into one or more
smaller buffers, each with explicit types.  
[BuildAssetBundlesParameters](BuildAssetBundlesParameters.html)| Provide
various options to control the behavior of BuildPipeline.BuildAssetBundles.  
[BuildFile](Build.Reporting.BuildFile.html)| Contains information about a
single file produced by the build process.  
[BuildPlayerOptions](BuildPlayerOptions.html)| Provide various options to
control the behavior of BuildPipeline.BuildPlayer.  
[BuildPlayerWithProfileOptions](BuildPlayerWithProfileOptions.html)| Provide
various options to control the behavior of BuildPipeline.BuildPlayer when
using a build profile.  
[BuildSettings](Build.Content.BuildSettings.html)| Struct containing
information on how to build content.  
[BuildStep](Build.Reporting.BuildStep.html)|  Contains information about a
single step in the build process. Additional resources: BuildReport.steps  
[BuildStepMessage](Build.Reporting.BuildStepMessage.html)|  Contains
information about a single log message recorded during the build process.
Additional resources: BuildStep.messages  
[BuildSummary](Build.Reporting.BuildSummary.html)| Contains overall summary
information about a build.  
[BuildUsageTagGlobal](Build.Content.BuildUsageTagGlobal.html)| Container for
holding information about lighting information being used in a build.  
[CacheServerConnectionChangedParameters](CacheServerConnectionChangedParameters.html)|
Struct used for AssetDatabase.cacheServerConnectionChanged.  
[CameraProjectionCache](CameraProjectionCache.html)| Project points from world
to screen space.  
[ChangeAssetObjectPropertiesEventArgs](ChangeAssetObjectPropertiesEventArgs.html)|
A change of this type indicates that a property of an asset object in memory
has changed. This happens for example when Undo.RecordObject is used with an
instance of an asset (e.g. Texture). Note that this only covers changes to
asset objects in memory and not changes to assets in the project on disk.  
[ChangeChildrenOrderEventArgs](ChangeChildrenOrderEventArgs.html)| A change of
this type indicates that a GameObject's children have been reordered. This
happens when Undo.RegisterChildrenOrderUndo is called or when reordering a
child in the hierarchy under the same parent.  
[ChangeGameObjectOrComponentPropertiesEventArgs](ChangeGameObjectOrComponentPropertiesEventArgs.html)|
A change of this type indicates that a property of a GameObject or Component
has changed. This happens for example when Undo.RecordObject is used with an
instance of a Component.  
[ChangeGameObjectParentEventArgs](ChangeGameObjectParentEventArgs.html)| A
change of this type indicates that the parent of a GameObject has changed.
This happens when Undo.SetTransformParent or
SceneManager.MoveGameObjectToScene is used.  
[ChangeGameObjectStructureEventArgs](ChangeGameObjectStructureEventArgs.html)|
A change of this type indicates that the structure of a GameObject has
changed. This happens when a component is added to or removed from the
GameObject using Undo.AddComponent or Undo.DestroyObjectImmediate.  
[ChangeGameObjectStructureHierarchyEventArgs](ChangeGameObjectStructureHierarchyEventArgs.html)|
A change of this type indicates that the structure of a GameObject has changed
and any GameObject in the hierarchy below it might have changed. This happens
for example when Undo.RegisterFullObjectHierarchyUndo is used.  
[ChangeRootOrderEventArgs](ChangeRootOrderEventArgs.html)| A change of this
type indicates that a GameObject placed at the scene root has been reordered.
This happens when Undo.SetSiblingIndex is called or when reordering a root
GameObject in the hierarchy under the same parent.  
[ChangeSceneEventArgs](ChangeSceneEventArgs.html)| A change of this type
indicates that an open scene has been changed ("dirtied") without any more
specific information available. This happens for example when
EditorSceneManager.MarkSceneDirty is used.  
[ChannelClientInfo](MPE.ChannelClientInfo.html)| A structure that contains all
of a ChannelClient's connection data.  
[ChannelClientScope](MPE.ChannelClientScope.html)| Scope that can be use to
open a channel client on a specific channel and close the channel when the
scope ends.  
[ChannelInfo](MPE.ChannelInfo.html)| A structure that contains the connection
information of a Channel in ChannelService.  
[ChannelScope](MPE.ChannelScope.html)| Scope that cna be use to open a channel
and that will close the channel when the scope ends.  
[ChildAnimatorState](Animations.ChildAnimatorState.html)| Structure that
represents a state in the context of its parent state machine.  
[ChildAnimatorStateMachine](Animations.ChildAnimatorStateMachine.html)|
Structure that represents a state machine in the context of its parent state
machine.  
[ChildMotion](Animations.ChildMotion.html)| Structure that represents a motion
in the context of its parent blend tree.  
[ClipAnimationInfoCurve](ClipAnimationInfoCurve.html)| Stores a curve and its
name that will be used to create additional curves during the import process.  
[CompilerMessage](Compilation.CompilerMessage.html)| Compiler Message.  
[ContentBuildProfileEvent](Build.Content.ContentBuildProfileEvent.html)|
Details about a profile event captured using the
ContentBuildInterface.BeginProfileCapture and
ContentBuildInterface.EndProfileCapture APIs.  
[CreateAssetObjectEventArgs](CreateAssetObjectEventArgs.html)| A change of
this type indicates that an asset object has been created. This happens for
example when Undo.RegisterCreatedObjectUndo is used with an instance of an
asset (e.g. Texture). Note that this only covers creation of asset objects in
memory and not creation of new assets in the project on disk.  
[CreateGameObjectHierarchyEventArgs](CreateGameObjectHierarchyEventArgs.html)|
A change of this type indicates that a GameObject has been created, possibly
with additional objects below it in the hierarchy. This happens for example
when Undo.RegisterCreatedObjectUndo is used with a GameObject.  
[CurveFilterOptions](Animations.CurveFilterOptions.html)| The keyframe
reduction settings for compressing animation curves.  
[CustomObjectIndexerTarget](Search.CustomObjectIndexerTarget.html)| Represents
a descriptor for the object that is about to be indexed. It stores a reference
to the object itself as well as an already set up SerializedObject.  
[DataModeChangeEventArgs](DataModeChangeEventArgs.html)| Container for the
different parameters of the IDataModeController.dataModeChanged event.  
[DefaultPreset](Presets.DefaultPreset.html)| This structure defines a default
Preset. See Preset.GetDefaultListForType and Preset.SetDefaultListForType for
usage.  
[DependencyInfo](PackageManager.DependencyInfo.html)| Structure describing
dependencies to other packages in PackageInfo.  
[DestroyAssetObjectEventArgs](DestroyAssetObjectEventArgs.html)| A change of
this type indicates that an asset object has been destroyed. This happens for
example when Undo.DestroyObjectImmediate is used with an instance of an asset
(e.g. Texture). Note that this only covers destruction of asset objects in
memory and not deletion of assets in the project on disk.  
[DestroyGameObjectHierarchyEventArgs](DestroyGameObjectHierarchyEventArgs.html)|
A change of this type indicates that a GameObject and the entire hierarchy
below it has been destroyed. This happens for example when
Undo.DestroyObjectImmediate is used with an GameObject.  
[DetailBrushBounds](TerrainTools.DetailBrushBounds.html)| Represents a
container for brush bound data.  
[DragAndDropWindowTarget](DragAndDropWindowTarget.html)| IDs for core windows.
These are used by the DragAndDrop.RemoveHandler API.  
[EditorCurveBinding](EditorCurveBinding.html)| Defines how a curve is attached
to an object that it controls.  
[EventID](LightTransport.EventID.html)| The EventID is used to keep track of
asynchronous operations executing on a context. The ID describes the unique
identifier of an event.  
[ExternalFileReference](Build.Content.ExternalFileReference.html)| Desribes an
externally referenced file. This is returned as part of the WriteResult when
writing a serialized file.  
[GameManagerDependencyInfo](Build.Content.GameManagerDependencyInfo.html)|
Contains dependency information for internal Unity game manager classes. Call
ContentBuildInterface.WriteGameManagersSerializedFile or
ContentBuildInterface.CalculatePlayerDependenciesForGameManagers to get an
instance of this class.  
[GlobalObjectId](GlobalObjectId.html)| Unique and stable project-scoped
identifier for objects in scenes and in other types of assets for use at
authoring time.  
[GpuBvhBuildOptions](Embree.GpuBvhBuildOptions.html)| Options for bounding
volume hierarchy (BVH) build.  
[GpuBvhPrimitiveDescriptor](Embree.GpuBvhPrimitiveDescriptor.html)|
Characteristics of a primitive used in the BVH build.  
[GraphViewChange](Experimental.GraphView.GraphViewChange.html)| Set of changes
in the graph that can be intercepted.  
[H264EncoderAttributes](Media.H264EncoderAttributes.html)| Descriptor for
H.264 encoder attributes.  
[InSceneAssetInformation](InSceneAssetInformation.html)| Provides information
related to an in-scene asset collected during a
InSceneAssetUtility.CollectInSceneAssets call.  
[KeyCombination](ShortcutManagement.KeyCombination.html)| Represents a
combination of a non-modifier key and zero or more modifier keys.  
[ManagedReferenceMissingType](ManagedReferenceMissingType.html)| Represents a
managed reference object that has a missing type.  
[MediaRational](Media.MediaRational.html)| Rational number useful for
expressing fractions precisely.  
[MediaTime](Media.MediaTime.html)| Time representation for use with media
containers.  
[NamedBuildTarget](Build.NamedBuildTarget.html)| Build Target by name. This
allows to describe and identify build targets that are not fully represented
by BuildTargetGroup and BuildTarget.  
[NodeCreationContext](Experimental.GraphView.NodeCreationContext.html)| This
struct represents the context when the user initiates creating a graph node.  
[ObjectChangeEventStream](ObjectChangeEventStream.html)| Represents a stream
of events that describes the changes applied to objects in memory over the
course of a frame.  
[ObjectIdentifier](Build.Content.ObjectIdentifier.html)| Struct that
identifies a specific object project wide.  
[ObjectSerializedInfo](Build.Content.ObjectSerializedInfo.html)| Struct
containing details about how an object was serialized.  
[PackedAssetInfo](Build.Reporting.PackedAssetInfo.html)| Contains information
about a single packed Asset.  
[ParseResult<T0>](Search.ParseResult_1.html)| A ParseResult represents the
result of a parsing operation.  
[PickingIncludeExcludeList](PickingIncludeExcludeList.html)| Represents a list
of Unity Object and DOTS Entity IDs that picking algorithms can either
consider or discard.  
[PresetType](Presets.PresetType.html)| Stores a type to which a Preset can be
applied.  
[ProfilerCategoryInfo](Profiling.ProfilerCategoryInfo.html)| Category
information descriptor structure.  
[ProfilerCounterDescriptor](Unity.Profiling.Editor.ProfilerCounterDescriptor.html)|
Provides a descriptor for a Profiler counter.  
[PropertyDatabaseRecordKey](Search.PropertyDatabaseRecordKey.html)| The key of
a record that is stored in the PropertyDatabase.  
[QueryFilterOperator](Search.QueryFilterOperator.html)| A QueryFilterOperator
defines a boolean operator between a value returned by a filter and an operand
inputted in the search query.  
[QueryGraphOptimizationOptions](Search.QueryGraphOptimizationOptions.html)|
Structure containing the different options used to optimize a query graph.  
[QueryToken](Search.QueryToken.html)| Represents a token of a query string.  
[QueryValidationOptions](Search.QueryValidationOptions.html)| Struct
containing the available query validation options.  
[RenderPickingArgs](RenderPickingArgs.html)| Provides information about what
is expected to render during the current picking rendering callback.  
[RenderPickingResult](RenderPickingResult.html)| This struct contains
information to notify Unity the outcome of this render picking callback.  
[ResourceFile](Build.Content.ResourceFile.html)| Details about a specific file
written by the ContentBuildInterface.WriteSerializedFile or
ContentBuildInterface.WriteSceneSerializedFile APIs.  
[Sample](PackageManager.UI.Sample.html)| Struct for Package Sample.  
[SceneDependencyInfo](Build.Content.SceneDependencyInfo.html)| Scene
dependency information generated from the ContentBuildInterface.PrepareScene
API.  
[SceneStateHash](Experimental.Rendering.SceneStateHash.html)| This class
contains hashes that represents the Scene state.  
[ScenesUsingAsset](Build.Reporting.ScenesUsingAsset.html)| Contains
information about which scenes in a build have references to an Asset in the
build.  
[ScriptCompilationResult](Build.Player.ScriptCompilationResult.html)| Struct
with result information returned from the
PlayerBuildInterface.CompilePlayerScripts API.  
[ScriptCompilationSettings](Build.Player.ScriptCompilationSettings.html)|
Struct containing information on how to build scripts.  
[SearchColumnCompareArgs](Search.SearchColumnCompareArgs.html)| Search column
compare arguments are used by SearchColumn.comparer to sort search results.  
[SearchColumnEventArgs](Search.SearchColumnEventArgs.html)| Search column
event arguments are used by SearchColumn.getter, SearchColumn.drawer and
SearchColumn.setter delegates.  
[SearchDocument](Search.SearchDocument.html)| Represents a searchable document
that has been indexed.  
[SearchExpressionContext](Search.SearchExpressionContext.html)| This context
encapsulate all the datas needed to evaluate a SearchExpression and it allows
user to interact with the evaluation runtime of an expression. A
SearchExpressionContext is created automatically with a
SearchExpressionRuntime anytime SearchExpression.Execute is called.  
[SearchExpressionRuntime](Search.SearchExpressionRuntime.html)| Encapsulate
all the runtime data needed to evaluate a root expression and all its
parameters. This class contains the SearchContext that created the root
SearchExpression and all the stack frames needed to evaluate all the nested
SearchExpression.  
[SearchField](Search.SearchField.html)| Search item field used by the property
table and selector systems.  
[SearchMonitorView](Search.SearchMonitorView.html)| Scoped search monitor
view.  
[SearchProposition](Search.SearchProposition.html)| Search propositions are
used to display choices to the user to add new filters to a search query.  
[SearchResult](Search.SearchResult.html)| Contains a SearchItem that was
retrieved from a query.  
[SearchSelectorArgs](Search.SearchSelectorArgs.html)| Search selector
arguments used when the search selector callback is invoked.  
[SearchValue](Search.SearchValue.html)| Search value is used to extend a query
engine with custom type parsers and filters to search results by value.  
[SearchWindowContext](Experimental.GraphView.SearchWindowContext.html)| This
structure includes parameters for configuring the search window.  
[SerializedLocation](Build.Content.SerializedLocation.html)| Struct containing
information about where an object was serialized.  
[ShaderCompilerData](Rendering.ShaderCompilerData.html)| Collection of data
used for shader variants generation, including targeted platform data and the
keyword set representing a specific shader variant.  
[ShaderInfo](ShaderInfo.html)| Contains the following information about a
shader: -If the shader has compilation errors or warnings. -If the shader is
supported on the currently selected platform. -The name of the shader.  
[ShaderMessage](ShaderMessage.html)| Contains information about messages
generated by Unity's Shader Compiler.  
[ShaderSnippetData](Rendering.ShaderSnippetData.html)| Collection of
properties about the specific shader code being compiled.  
[ShortcutArguments](ShortcutManagement.ShortcutArguments.html)| Provides data
for shortcut action methods invoked by the shortcut system.  
[ShortcutBinding](ShortcutManagement.ShortcutBinding.html)| Represents a key
binding used to trigger a shortcut.  
[ShortcutBindingChangedEventArgs](ShortcutManagement.ShortcutBindingChangedEventArgs.html)|
Provides data for the IShortcutManager.shortcutBindingChanged event.  
[SketchUpImportCamera](SketchUpImportCamera.html)| Structure to hold camera
data extracted from a SketchUp file.  
[SketchUpImportScene](SketchUpImportScene.html)| Structure to hold scene data
extracted from a SketchUp file.  
[SpriteAtlasPackingSettings](U2D.SpriteAtlasPackingSettings.html)| Settings to
use during the packing process for this SpriteAtlas.  
[SpriteAtlasTextureSettings](U2D.SpriteAtlasTextureSettings.html)| Texture
settings for the packed texture generated by SpriteAtlas.  
[SpriteImportData](AssetImporters.SpriteImportData.html)| Struct that
represents how Sprite asset should be generated when calling
TextureGenerator.GenerateTexture.  
[SpriteMetaData](SpriteMetaData.html)| Editor data used in producing a Sprite.  
[StageHandle](SceneManagement.StageHandle.html)| Struct that represents a
stage handle.  
[StringView](Search.StringView.html)| Structure that holds a view on a string,
with a specified range of [startIndex, endIndex[.  
[TakeInfo](TakeInfo.html)| A Takeinfo object contains all the information
needed to describe a take.  
[TextureGenerationOutput](AssetImporters.TextureGenerationOutput.html)|
Structure that represents the result from calling
TextureGenerator.GenerateTexture.  
[TextureGenerationSettings](AssetImporters.TextureGenerationSettings.html)|
Represents how a texture should be generated from calling
TextureGenerator.GenerateTexture.  
[TexturePropertyDescription](AssetImporters.TexturePropertyDescription.html)|
Contains a set of typed properties for describing a texture input of a
MaterialDescription.  
[TierSettings](Rendering.TierSettings.html)| A struct that represents graphics
settings for a given build target and graphics tier.  
[TouchEvent](DeviceSimulation.TouchEvent.html)| Representation of a single
touch event coming from a Device Simulator. Subscribe to
DeviceSimulator.touchScreenInput to receive these events.  
[UndoPropertyModification](UndoPropertyModification.html)| Additional
resources: Undo.postprocessModifications.  
[UndoRedoInfo](UndoRedoInfo.html)| Additional resources: Undo.undoRedoEvent.  
[UnwrapParam](UnwrapParam.html)| Unwrapping settings.  
[UpdatePrefabInstancesEventArgs](UpdatePrefabInstancesEventArgs.html)| A
change of this type indicates that prefab instances in an open scene have been
updated due to a change to the source prefab.  
[VideoTrackAttributes](Media.VideoTrackAttributes.html)| Descriptor for audio
track format.  
[VideoTrackEncoderAttributes](Media.VideoTrackEncoderAttributes.html)|
Descriptor for video track format.  
[VP8EncoderAttributes](Media.VP8EncoderAttributes.html)| Descriptor for VP8
encoder attributes.  
[WriteManagerParameters](Build.Content.WriteManagerParameters.html)| Defines
the write parameters for the
ContentBuildInterface.WriteGameManagersSerializedFile function.  
[WriteParameters](Build.Content.WriteParameters.html)| This struct collects
all the WriteSerializedFile parameters in to a single place.  
[WriteResult](Build.Content.WriteResult.html)| Struct containing the results
from the ContentBuildPipeline.WriteSerialziedFile and
ContentBuildPipeline.WriteSceneSerialziedFile APIs.  
[WriteSceneParameters](Build.Content.WriteSceneParameters.html)| This struct
collects all the WriteSceneSerializedFile parameters in to a single place.  
  
### Enumerations

[ActionOnDotNetUnhandledException](ActionOnDotNetUnhandledException.html)| The
behavior in case of unhandled .NET exception.  
---|---  
[AdvancedObjectSelectorEventType](SearchService.AdvancedObjectSelectorEventType.html)|
Enum that defines the type of events that are possible when calling a custom
advanced object selector.  
[AndroidApplicationEntry](AndroidApplicationEntry.html)| Options for which
application entries to include when Unity generates a Gradle project.  
[AndroidArchitecture](AndroidArchitecture.html)| Android CPU architecture.  
[AndroidAutoRotationBehavior](AndroidAutoRotationBehavior.html)| Options to
control the application window orientation when Default orientation is set to
Auto rotation.  
[AndroidBlitType](AndroidBlitType.html)| Describes the method for how content
is displayed on the screen.  
[AndroidBuildSystem](AndroidBuildSystem.html)| Type of Android build system.  
[AndroidBuildType](AndroidBuildType.html)| Build configurations for the
generated project.  
[AndroidCreateSymbols](AndroidCreateSymbols.html)| Defines the options
available for choosing the type of symbol file to create in an Android build.  
[AndroidETC2FallbackOverride](AndroidETC2FallbackOverride.html)| This
enumeration has values for different qualities to decompress an ETC2 texture
on Android devices that don't support the ETC2 texture format.  
[AndroidGamepadSupportLevel](AndroidGamepadSupportLevel.html)| Gamepad support
level for Android TV.  
[AndroidPreferredInstallLocation](AndroidPreferredInstallLocation.html)|
Preferred application install location.  
[AndroidSdkVersions](AndroidSdkVersions.html)| API levels that can be
specified in scripts. Note that the lowest API level here strictly corresponds
to the lowest supported API level, however these values should not be used to
determine the highest supported API level.  
[AndroidShowActivityIndicatorOnLoading](AndroidShowActivityIndicatorOnLoading.html)|
Application should show ActivityIndicator when loading.  
[AndroidSplashScreenScale](AndroidSplashScreenScale.html)| Android splash
screen scale modes.  
[AnimatorConditionMode](Animations.AnimatorConditionMode.html)| The mode of
the condition.  
[AnimatorLayerBlendingMode](Animations.AnimatorLayerBlendingMode.html)|
Specifies how the layer is blended with the previous layers.  
[ApiCompatibilityLevel](ApiCompatibilityLevel.html)| .NET API compatibility
level.  
[AppleMobileArchitecture](AppleMobileArchitecture.html)| Apple Mobile CPU
architecture.  
[AppleMobileArchitectureSimulator](AppleMobileArchitectureSimulator.html)|
Apple mobile CPU architecture options for the Simulator.  
[AscentCalculationMode](AscentCalculationMode.html)| Method used for
calculating a font's ascent.  
[AssembliesType](Compilation.AssembliesType.html)| Flags for Assembly.  
[AssemblyBuilderFlags](Compilation.AssemblyBuilderFlags.html)| Flags used by
AssemblyBuilder to control assembly build.  
[AssemblyBuilderStatus](Compilation.AssemblyBuilderStatus.html)| Status of the
AssemblyBuilder build.  
[AssemblyDefinitionReferenceType](Compilation.AssemblyDefinitionReferenceType.html)|
Assembly definition file reference type.  
[AssemblyFlags](Compilation.AssemblyFlags.html)| Flags for Assembly.  
[AssetDeleteResult](AssetDeleteResult.html)| Result of Asset delete operation  
[AssetMoveResult](AssetMoveResult.html)| Result of Asset move  
[AssetPathToGUIDOptions](AssetPathToGUIDOptions.html)| Asset path to GUID
options.  
[AssetPipelineMode](AssetPipelineMode.html)| Selects the Assetpipeline mode to
use.  
[AudioSampleRateSetting](AudioSampleRateSetting.html)| The sample rate setting
used within the AudioImporter. This defines the sample rate conversion of
audio on import.  
[BatchRendererGroupStrippingMode](Rendering.BatchRendererGroupStrippingMode.html)|
Enum of the different modes of operation for BatchRendererGroup shader variant
stripping.  
[BlendTreeType](Animations.BlendTreeType.html)| The type of blending algorithm
that the blend tree uses.  
[BrushGUIEditFlags](TerrainTools.BrushGUIEditFlags.html)| Flags that specify
which brush controls the [IOnInspectorGUI.ShowBrushesGUI] method displays.  
[BuildAssetBundleOptions](BuildAssetBundleOptions.html)| Asset Bundle building
options.  
[BuildOptions](BuildOptions.html)| Building options. Multiple options can be
combined together.  
[BuildResult](Build.Reporting.BuildResult.html)| Describes the outcome of the
build process.  
[BuildTarget](BuildTarget.html)| Target build platform.  
[BuildTargetGroup](BuildTargetGroup.html)| Build target group.  
[BuildType](Build.Reporting.BuildType.html)| Build type.  
[CacheServerMode](CacheServerMode.html)| Selects the cache server
configuration mode.  
[CacheServerValidationMode](CacheServerValidationMode.html)| Options for the
accelerate server validation mode.  
[CanAppendBuild](CanAppendBuild.html)| Whether you can append an existing
build using BuildOptions.AcceptExternalModificationsToPlayer.  
[Capabilities](Experimental.GraphView.Capabilities.html)| Capabilities used by
Manipulators to easily determine valid actions on a GraphElement.  
[CheckoutMode](VersionControl.CheckoutMode.html)| What to checkout when
starting the Checkout task through the version control Provider.  
[ClipAnimationMaskType](ClipAnimationMaskType.html)| AnimationClip mask
options for ModelImporterClipAnimation.  
[CodeOptimization](Compilation.CodeOptimization.html)| Code optimization mode
defines whether UnityEditor compiles scripts in Debug or Release mode.  
[CompilerMessageType](Compilation.CompilerMessageType.html)| Compiler message
type.  
[CompletionAction](VersionControl.CompletionAction.html)| Different actions a
version control task can do upon completion.  
[ContentBuildFlags](Build.Content.ContentBuildFlags.html)| Build options for
content.  
[CoppaCompliance](CoppaCompliance.html)| The enumerated states of the
project's Coppa compliance setting.  
[D3D11FullscreenMode](D3D11FullscreenMode.html)| Direct3D 11 fullscreen mode.  
[DataMode](DataMode.html)| Options for the different DataModes of an
EditorWindow.  
[DependencyType](Build.Content.DependencyType.html)| Dependency calculation
flags to control what is returned, and how it operates.  
[DialogOptOutDecisionType](DialogOptOutDecisionType.html)| The type of opt-out
decision a user can make.  
[Direction](Experimental.GraphView.Direction.html)| Port direction (in or
out).  
[DisplayMode](Search.DisplayMode.html)| Options for setting the display mode
to use for a search view.  
[DockPosition](Overlays.DockPosition.html)| DockPosition describes the
alignment of an Overlay within a DockZone.  
[DockZone](Overlays.DockZone.html)| DockZone describes the area of the screen
that an Overlay is displayed in.  
[DragAndDropVisualMode](DragAndDropVisualMode.html)| Visual indication mode
for Drag & Drop operation.  
[DrawCameraMode](DrawCameraMode.html)| Drawing modes for Handles.DrawCamera.  
[EditorActionResult](Actions.EditorActionResult.html)| The state that the
EditorAction was completed in.  
[EditorAssembliesCompatibilityLevel](EditorAssembliesCompatibilityLevel.html)|
.NET API compatibility level.  
[EditorSelectedRenderState](EditorSelectedRenderState.html)| The editor
selected render mode for Scene View selection.  
[EditorSkin](EditorSkin.html)| Enum that selects which skin to return from
EditorGUIUtility.GetBuiltinSkin.  
[EnterPlayModeOptions](EnterPlayModeOptions.html)| Determines the flags for
the Enter Play Mode Options in the Unity Editor.  
[ErrorCode](PackageManager.ErrorCode.html)| Package operation Error.  
[EventDataSerialization](MPE.EventDataSerialization.html)| The Serialization
type for sending a message, with arguments, using the EventService. For more
information about argument serialization, see ChannelService.Broadcast and
ChannelService.Emit.  
[EventPropagation](Experimental.GraphView.EventPropagation.html)| Value that
determines if a event handler stops propagation of events or allows it to
continue.  
[ExportPackageOptions](ExportPackageOptions.html)| Export package option. Multiple options can be combined together using the | operator.  
[FetchPreviewOptions](Search.FetchPreviewOptions.html)| Options for the search
provider on how the preview should be fetched.  
[FileMode](VersionControl.FileMode.html)| Mode of the file.  
[FileType](Build.Content.FileType.html)| Enum description of the type of file
an object comes from.  
[FilterAction](ShaderKeywordFilter.FilterAction.html)| Whether shader keyword
filter attributes include the keywords, remove the keywords or do nothing,
based on the attribute condition evaluation.  
[FoliageIndex](TerrainTools.FoliageIndex.html)| The index at which you should
place the foliage tools in the Terrain Tools overlay.  
[FontRenderingMode](FontRenderingMode.html)| Font rendering mode constants for
TrueTypeFontImporter.  
[FontTextureCase](FontTextureCase.html)| Texture case constants for
TrueTypeFontImporter.  
[ForceReserializeAssetsOptions](ForceReserializeAssetsOptions.html)| Options
for AssetDatabase.ForceReserializeAssets.  
[GfxThreadingMode](GfxThreadingMode.html)| Enum used to specify the threading
mode to use.  
[GizmoType](GizmoType.html)| Determines how a gizmo is drawn or picked in the
Unity editor.  
[GpuBvhBuildQuality](Embree.GpuBvhBuildQuality.html)| BVH build quality.  
[GraphicsJobMode](GraphicsJobMode.html)| Enum used to specify the graphics
jobs mode to use.  
[HierarchyDropFlags](HierarchyDropFlags.html)| Define how dragged objects
should be dropped relative to already existing Hierarchy items.  
[HighlightSearchMode](HighlightSearchMode.html)| Used to specify how to find a
given element in the editor to highlight.  
[IconKind](IconKind.html)| Icon kind.  
[IconOverlayType](VersionControl.IconOverlayType.html)| Type of icon overlay.  
[Il2CppCodeGeneration](Build.Il2CppCodeGeneration.html)| Options to control
code generation for IL2CPP compiler.  
[Il2CppCompilerConfiguration](Il2CppCompilerConfiguration.html)| C++ compiler
configuration used when compiling IL2CPP generated code.  
[Il2CppStacktraceInformation](Il2CppStacktraceInformation.html)| Stack trace
information options to choose how much information to include in IL2CPP
generated stack traces.  
[ImportAssetOptions](ImportAssetOptions.html)| Asset importing options.  
[ImportLogFlags](AssetImporters.ImportLogFlags.html)| A value indicating the
severity of an import log.  
[IndexingOptions](Search.IndexingOptions.html)| Use Indexing options to
specify the contents of your search index.  
[InsecureHttpOption](InsecureHttpOption.html)| Options for allowing plain text
HTTP connections for UnityWebRequest.  
[InteractionMode](InteractionMode.html)| The mode of interaction, user or
automated, that an API method is called with.  
[iOSAppInBackgroundBehavior](iOSAppInBackgroundBehavior.html)| Application
behavior when entering background.  
[iOSBackgroundMode](iOSBackgroundMode.html)| Background modes supported by the
application corresponding to project settings in Xcode.  
[iOSLaunchScreenImageType](iOSLaunchScreenImageType.html)| iOS launch screen
settings.  
[iOSLaunchScreenType](iOSLaunchScreenType.html)| iOS launch screen settings.  
[iOSSdkVersion](iOSSdkVersion.html)| Supported iOS SDK versions.  
[iOSShowActivityIndicatorOnLoading](iOSShowActivityIndicatorOnLoading.html)|
Activity Indicator on loading.  
[iOSStatusBarStyle](iOSStatusBarStyle.html)| iOS status bar style.  
[iOSTargetDevice](iOSTargetDevice.html)| Target iOS device.  
[Layout](Overlays.Layout.html)| Possible layouts for an overlay.  
[LineEndingsMode](LineEndingsMode.html)| Defines the type of line endings used
when creating new C# files from within the editor.  
[LogLevel](PackageManager.LogLevel.html)| Describes different levels of log
information the Package Manager supports.  
[MacFullscreenMode](MacFullscreenMode.html)| Mac fullscreen mode.  
[ManagedStrippingLevel](ManagedStrippingLevel.html)| Defines how aggressively
Unity strips unused managed (C#) code.  
[MaterialIndex](TerrainTools.MaterialIndex.html)| The index at which you
should place the material tools in the Terrain Tools overlay.  
[MeshDeformation](MeshDeformation.html)| Specifies which method Unity uses to
process mesh deformations for skinning.  
[MeshOptimizationFlags](MeshOptimizationFlags.html)| Options to control the
optimization of mesh data during asset import.  
[MessageType](MessageType.html)| User message types.  
[MobileTextureSubtarget](MobileTextureSubtarget.html)| Compressed texture
format for target build platform.  
[ModelImporterAnimationCompression](ModelImporterAnimationCompression.html)|
Animation compression options for ModelImporter.  
[ModelImporterAnimationType](ModelImporterAnimationType.html)| Animation mode
for ModelImporter.  
[ModelImporterAvatarSetup](ModelImporterAvatarSetup.html)| Set the Avatar
generation mode for ModelImporter.  
[ModelImporterGenerateAnimations](ModelImporterGenerateAnimations.html)|
Animation generation options for ModelImporter. These options relate to the
legacy Animation system, they should only be used when
ModelImporter.animationType==ModelImporterAnimationType.Legacy.  
[ModelImporterHumanoidOversampling](ModelImporterHumanoidOversampling.html)|
Humanoid Oversampling available multipliers.  
[ModelImporterIndexFormat](ModelImporterIndexFormat.html)| Format of the
imported mesh index buffer data.  
[ModelImporterMaterialImportMode](ModelImporterMaterialImportMode.html)|
Material import options for ModelImporter.  
[ModelImporterMaterialLocation](ModelImporterMaterialLocation.html)| Material
import options for ModelImporter.  
[ModelImporterMaterialName](ModelImporterMaterialName.html)| Material naming
options for ModelImporter.  
[ModelImporterMaterialSearch](ModelImporterMaterialSearch.html)| Material
search options for ModelImporter.  
[ModelImporterMeshCompression](ModelImporterMeshCompression.html)| Mesh
compression options for ModelImporter.  
[ModelImporterNormalCalculationMode](ModelImporterNormalCalculationMode.html)|
Normal generation options for ModelImporter.  
[ModelImporterNormals](ModelImporterNormals.html)| Normal generation options
for ModelImporter.  
[ModelImporterNormalSmoothingSource](ModelImporterNormalSmoothingSource.html)|
Source of smoothing information for calculation of normals in ModelImporter.  
[ModelImporterSecondaryUVMarginMethod](ModelImporterSecondaryUVMarginMethod.html)|
Methods for handling margins during lightmap UV generation in ModelImporter.  
[ModelImporterSkinWeights](ModelImporterSkinWeights.html)| Skin weights
options for ModelImporter.  
[ModelImporterTangents](ModelImporterTangents.html)| Vertex tangent generation
options for ModelImporter.  
[ModelImporterTangentSpaceMode](ModelImporterTangentSpaceMode.html)| Tangent
space generation options for ModelImporter.  
[MouseCursor](MouseCursor.html)| Custom mouse cursor shapes used with
EditorGUIUtility.AddCursorRect.  
[NeighborTerrainsIndex](TerrainTools.NeighborTerrainsIndex.html)| The index at
which you should place the neighbor terrain tools in the Terrain Tools
overlay.  
[NewSceneMode](SceneManagement.NewSceneMode.html)| Used when creating a new
Scene in the Editor.  
[NewSceneSetup](SceneManagement.NewSceneSetup.html)| Used when creating a new
Scene in the Editor.  
[NormalMapEncoding](NormalMapEncoding.html)| Describes the encoding of normal
maps.  
[ObjectChangeKind](ObjectChangeKind.html)| This enumeration describes the
different kind of changes that can be tracked in an ObjectChangeEventStream.
Each event has a corresponding type in ObjectChangeEvents.  
[ObjectMatchMode](ObjectMatchMode.html)| Enum for controlling how e.g.
GameObjects and Components are matched.  
[ObjectSelectorSearchEndSessionModes](SearchService.ObjectSelectorSearchEndSessionModes.html)|
A bit field that contains the different modes to end an Object Selector Search
session.  
[OnlineState](VersionControl.OnlineState.html)| Represent the connection state
of the version control provider.  
[OnOpenAssetAttributeMode](Callbacks.OnOpenAssetAttributeMode.html)| Indicates
whether OnOpenAssetAttribute decorated method is a validation function that
checks if asset opening is handled by Unity or a custom script.  
[OpenSceneMode](SceneManagement.OpenSceneMode.html)| Used when opening a Scene
in the Editor to specify how a Scene should be opened.  
[Orientation](Experimental.GraphView.Orientation.html)| Graph element
orientation.  
[OSArchitecture](Build.OSArchitecture.html)| Enum representing processor
architectures that are supported by certain operating systems.  
[OverrideTextureCompression](Build.OverrideTextureCompression.html)| Sets
which texture compression override to use when importing assets.  
[PackageSource](PackageManager.PackageSource.html)| Source of packages.  
[PauseState](PauseState.html)| Enumeration specifying the current pause state
of the Editor.Additional resources: PlayModeStateChange,
EditorApplication.pauseStateChanged, EditorApplication.isPaused.  
[PivotMode](PivotMode.html)| Where is the tool handle placed.  
[PivotRotation](PivotRotation.html)| How is the tool handle oriented.  
[PlayerConnectionInitiateMode](PlayerConnectionInitiateMode.html)| Describes
how the player connects to the Editor.  
[PlayModeStateChange](PlayModeStateChange.html)| Enumeration specifying a
change in the Editor's play mode state.Additional resources: PauseState,
EditorApplication.playModeStateChanged, EditorApplication.isPlaying.  
[PrefabAssetType](PrefabAssetType.html)| Enum indicating the type of Prefab
Asset, such as Regular, Model and Variant.  
[PrefabInstanceStatus](PrefabInstanceStatus.html)| Enum with status about
whether a Prefab instance is properly connected to its asset.  
[PrefabOverridesOptions](PrefabOverridesOptions.html)| Flags that can be used
to control which overrides shoud be kept or cleared when using
ReplacePrefabAssetOfPrefabInstance.  
[PrefabUnpackMode](PrefabUnpackMode.html)| Enum used to determine how a Prefab
should be unpacked.  
[PreprocessorOverride](PreprocessorOverride.html)| This enum is now obsolete.
Unity always uses the Caching Shader Preprocessor.  
[ProcessEvent](MPE.ProcessEvent.html)| Enum that represents the events a
RoleProvider can receive.  
[ProcessLevel](MPE.ProcessLevel.html)| The type of the current process. It can
be a Unity master instance, or a secondary instance connected to the master.  
[ProcessState](MPE.ProcessState.html)| Describes the state of a specifc
UnityEditor process.  
[ProfileCaptureOptions](Build.Content.ProfileCaptureOptions.html)| Options for
filtering captured profile events using the
ContentBuildInterface.BeginProfileCapture and
ContentBuildInterface.EndProfileCapture APIs.  
[ProfileEventType](Build.Content.ProfileEventType.html)| Options for labelling
captured profile events using the ContentBuildInterface.BeginProfileCapture
and ContentBuildInterface.EndProfileCapture APIs.  
[ProfilerModuleChartType](Unity.Profiling.Editor.ProfilerModuleChartType.html)|
Options for a Profiler module’s chart type.  
[PropertyDatabaseType](Search.PropertyDatabaseType.html)| An enum representing
the type of data stored in a record.  
[ProvisioningProfileType](ProvisioningProfileType.html)| The type of the iOS
provisioning profile if manual signing is used.  
[QueryNodeType](Search.QueryNodeType.html)| Options for representing the query
node types.  
[ReferencesOptions](Compilation.ReferencesOptions.html)| Options to control
the Unity References to other assembly definition files that Unity uses during
compilation.  
[RefreshFlags](Search.RefreshFlags.html)| Refresh flags are used to indicate
why search view needs to be refreshed or updated.  
[RemoveAssetOptions](RemoveAssetOptions.html)| Options for removing assets  
[RenderPickingType](RenderPickingType.html)| Specifies the type of a render
picking callback.  
[RepaintFlags](TerrainTools.RepaintFlags.html)| Flags that indicate what to
repaint on the Terrain tools.  
[RequestScriptCompilationOptions](Compilation.RequestScriptCompilationOptions.html)|
Options for specifying the behavior of
CompilationPipeline.RequestScriptCompilation.  
[ResizerDirection](Experimental.GraphView.ResizerDirection.html)| Enum that
specifies in which direction to resize the element.  
[ResolveMethod](VersionControl.ResolveMethod.html)| How assets should be
resolved.  
[RevertMode](VersionControl.RevertMode.html)| Defines the behaviour of the
version control revert methods.  
[ScriptCallOptimizationLevel](ScriptCallOptimizationLevel.html)| Script call
optimization level.  
[ScriptCompilationOptions](Build.Player.ScriptCompilationOptions.html)| Script
compilation options.  
[ScriptingImplementation](ScriptingImplementation.html)| Scripting
implementation (backend).  
[SculptIndex](TerrainTools.SculptIndex.html)| The index at which you should
place the sculpt tools in the Terrain Tools overlay.  
[SearchColumnFlags](Search.SearchColumnFlags.html)| Search column flags are
used to set multiple states.  
[SearchDocumentFlags](Search.SearchDocumentFlags.html)| Search document flags
are used by the indexing system to provide additional information of an
indexed document, like its source.  
[SearchEngineScope](SearchService.SearchEngineScope.html)| An enumeration that
contains the available search engine scopes.  
[SearchExpressionEvaluationHints](Search.SearchExpressionEvaluationHints.html)|
Hints provided to the SearchExpression runtime to specify how a certain
SearchExpressionEvaluatorAttribute should be executed.  
[SearchExpressionKeyword](Search.SearchExpressionKeyword.html)| Enum contaning
all keywords used as configuration parameter in builtin evaluator of
SearchExpression.  
[SearchExpressionType](Search.SearchExpressionType.html)| Type used to
characterize an expression. An expression might have multiple types. For
example a Set is also an iterable. A keyword is also considered a string
value. SearchExpressionType can be used with
SearchExpressionEvaluatorAttribute to describe the parameter list of an
evaluator.  
[SearchFlags](Search.SearchFlags.html)| Search options used to fetch items.
Mostly with SearchContext to specify how a search should be handled.  
[SearchItemOptions](Search.SearchItemOptions.html)| Indicates how the search
item description needs to be formatted when presented to the user.  
[SearchPropositionFlags](Search.SearchPropositionFlags.html)| The search
proposition flags are used to give additional context to the search
proposition.  
[SearchQueryErrorType](Search.SearchQueryErrorType.html)| Enum representing
the possible types of query errors.  
[SelectionMode](SelectionMode.html)| SelectionMode can be used to tweak the
selection returned by Selection.GetTransforms.  
[SemanticMergeMode](SemanticMergeMode.html)| Behavior of semantic merge.  
[SerializedPropertyNumericType](SerializedPropertyNumericType.html)| Returns
the precise type for Integer or Floating point properties.  
[SerializedPropertyType](SerializedPropertyType.html)| Represents the type of
a SerializedProperty.  
[SettingsScope](SettingsScope.html)| Sets the scope of a SettingsProvider. The
Scope determines where it appears in the UI. For example, whether it appears
with the Project settings in the Settings window, or in the Preferences
window, or in both windows.  
[ShaderCompilerMessageSeverity](Rendering.ShaderCompilerMessageSeverity.html)|
Indicates the severity of a message returned by the Unity Shader Compiler.  
[ShaderCompilerPlatform](Rendering.ShaderCompilerPlatform.html)| Shader
compiler used to generate player data shader variants.  
[ShaderPrecisionModel](ShaderPrecisionModel.html)| Options for the shader
precision model.  
[ShaderQuality](Rendering.ShaderQuality.html)| Shader quality preset.  
[ShaderRequirements](Rendering.ShaderRequirements.html)| Shader features
required by a specific shader. Features are bit flags.  
[ShaderType](Rendering.ShaderType.html)| Identifies the stage in the rendering
pipeline.  
[ShortcutModifiers](ShortcutManagement.ShortcutModifiers.html)| Represents
modifier keys for use in a shortcut binding.  
[ShortcutStage](ShortcutManagement.ShortcutStage.html)| Represents the stage
at which a shortcut action was invoked.  
[ShowDetailsOptions](Search.ShowDetailsOptions.html)| Defines what details are
shown in the preview inspector panel for the search view.  
[SpriteImportMode](SpriteImportMode.html)| Texture importer modes for Sprite
import.  
[SpritePackerMode](SpritePackerMode.html)| Sprite Packer mode for the current
project.  
[StandaloneBuildSubtarget](StandaloneBuildSubtarget.html)| Desktop platform
subtarget type.  
[StaticEditorFlags](StaticEditorFlags.html)| Describes which Unity systems
consider the GameObject as static, and include the GameObject in their
precomputations in the Unity Editor.  
[StatusCode](PackageManager.StatusCode.html)| Unity Package Manager operation
status.  
[StatusQueryOptions](StatusQueryOptions.html)| Options for querying the
version control system status of a file.  
[StereoRenderingPath](StereoRenderingPath.html)| Enum used to specify what
stereo rendering path to use.  
[StickyNoteChange](Experimental.GraphView.StickyNoteChange.html)| Enum that
specifies the type of change to the [StickyNote].  
[StickyNoteFontSize](Experimental.GraphView.StickyNoteFontSize.html)| Enum
used to describe the font size used by the [StickyNote].  
[StickyNoteTheme](Experimental.GraphView.StickyNoteTheme.html)| Enum used to
describe the visual theme used by the [StickyNote].  
[StrippingLevel](StrippingLevel.html)| Managed code stripping level.  
[SubmitResult](VersionControl.SubmitResult.html)| The status of an operation
returned by the VCS.  
[TemplateInstantiationMode](SceneTemplate.TemplateInstantiationMode.html)| An
enumeration of options for handling a Scene dependency Asset when you
instantiate a SceneTemplateAsset.  
[TerrainBrushPreviewMode](TerrainTools.TerrainBrushPreviewMode.html)| Enum to
specify whether DrawBrushPreview previews the source render texture or the
destination render texture of a PaintContext.  
[TerrainCategory](TerrainTools.TerrainCategory.html)| A category with which to
define tools that inherit from the ITerrainPaintToolWithOverlays interface.  
[TerrainDetailMeshRenderMode](TerrainDetailMeshRenderMode.html)| Options for
determining the render mode of the mesh detail.  
[TextCursorPlacement](Search.TextCursorPlacement.html)| Where to place the
cursor in the text. (see ISearchView.SetSearchText).  
[TextureCompressionFormat](TextureCompressionFormat.html)| Options for the
compressed texture formats that are available on the target build platform.  
[TextureCompressionQuality](TextureCompressionQuality.html)| Compression
Quality.  
[TextureImporterAlphaSource](TextureImporterAlphaSource.html)| Select how the
alpha of the imported texture is generated.  
[TextureImporterCompression](TextureImporterCompression.html)| Select the kind
of compression you want for your texture.  
[TextureImporterCubemapConvolution](TextureImporterCubemapConvolution.html)|
Defines Cubemap convolution mode.  
[TextureImporterFormat](TextureImporterFormat.html)| Imported texture format
for TextureImporter.  
[TextureImporterGenerateCubemap](TextureImporterGenerateCubemap.html)| Cubemap
generation mode for TextureImporter.  
[TextureImporterMipFilter](TextureImporterMipFilter.html)| Mip map filter for
TextureImporter.  
[TextureImporterNormalFilter](TextureImporterNormalFilter.html)| Normal map
filtering mode for TextureImporter.  
[TextureImporterNPOTScale](TextureImporterNPOTScale.html)| Scaling mode for
non power of two textures in TextureImporter.  
[TextureImporterRGBMMode](TextureImporterRGBMMode.html)| RGBM encoding mode
for HDR textures in TextureImporter.  
[TextureImporterShape](TextureImporterShape.html)| The shape of the imported
texture.  
[TextureImporterSingleChannelComponent](TextureImporterSingleChannelComponent.html)|
Selects which Color/Alpha channel Single Channel Textures uses.  
[TextureImporterSwizzle](TextureImporterSwizzle.html)| Options for where
texture color channel data comes from in the TextureImporter.  
[TextureImporterType](TextureImporterType.html)| Select this to set basic
parameters depending on the purpose of your texture.  
[TextureResizeAlgorithm](TextureResizeAlgorithm.html)| For Texture to be
scaled down choose resize algorithm. ( Applyed only when Texture dimension is
bigger than Max Size ).  
[Tool](Tool.html)| Which tool is active in the editor.  
[TouchPhase](DeviceSimulation.TouchPhase.html)| Indicates where in its
lifecycle a given touch is.  
[TransitionInterruptionSource](Animations.TransitionInterruptionSource.html)|
Which AnimatorState transitions can interrupt the Transition.  
[TreeViewSelectionOptions](IMGUI.Controls.TreeViewSelectionOptions.html)| Enum
used by the TreeView.SetSelection method.  
[tvOSSdkVersion](tvOSSdkVersion.html)| Supported tvOS SDK versions.  
[UIOrientation](UIOrientation.html)| Default mobile device orientation.  
[VertexChannelCompressionFlags](VertexChannelCompressionFlags.html)| Use these
enum flags to specify which elements of a vertex to compress.  
[VideoBitrateMode](VideoBitrateMode.html)| Bit rate after the clip is
transcoded.  
[VideoCodec](VideoCodec.html)| Video codec to use when importing video clips.  
[VideoDeinterlaceMode](VideoDeinterlaceMode.html)| Describes how the fields in
the image, if any, should be interpreted.  
[VideoEncodeAspectRatio](VideoEncodeAspectRatio.html)| Methods to compensate
for aspect ratio discrepancies between the source resolution and the wanted
encoding size.  
[VideoEncodingProfile](VideoEncodingProfile.html)| Options for the encoder
profile.  
[VideoResizeMode](VideoResizeMode.html)| How the video clip's images will be
resized during transcoding.  
[VideoSpatialQuality](VideoSpatialQuality.html)| Controls the imported clip's
internal resize to save space at the cost of blurrier images.  
[ViewTool](ViewTool.html)| Enum for Tools.viewTool.  
[VisibleObjects](SearchService.VisibleObjects.html)| A bit field that contains
the different categories of object that the object selector window can
display.  
[VisionOSSdkVersion](VisionOSSdkVersion.html)| Supported VisionOS SDK
versions.  
[WebGLClientBrowserType](WebGLClientBrowserType.html)| An enum containing the
supported client web browsers.  
[WebGLCompressionFormat](WebGLCompressionFormat.html)| An enum containing
different compression types.  
[WebGLDebugSymbolMode](WebGLDebugSymbolMode.html)| An enum containing
different modes for debug symbols.  
[WebGLExceptionSupport](WebGLExceptionSupport.html)| Options for Exception
support in WebGL.  
[WebGLLinkerTarget](WebGLLinkerTarget.html)| The build format options
available when building to WebGL.  
[WebGLMemoryGrowthMode](WebGLMemoryGrowthMode.html)| An enum containing
different memory growth modes.  
[WebGLPowerPreference](WebGLPowerPreference.html)| An enum containing
different power preference hints for the WebGL context.  
[WebGLTextureSubtarget](WebGLTextureSubtarget.html)| Compressed texture format
for target build platform.  
[WebGLWasmArithmeticExceptions](WebGLWasmArithmeticExceptions.html)| An enum
containing different trapping modes for WebAssembly code.  
[WindowsBuildAndRunDeployTarget](WindowsBuildAndRunDeployTarget.html)|
Specifies which Windows device to deploy and launch the Windows app on when
using Build and Run from the Editor.  
[WindowsGamepadBackendHint](WindowsGamepadBackendHint.html)| Specifies the
desired Windows API to be used for input.  
[WSABuildAndRunDeployTarget](WSABuildAndRunDeployTarget.html)| Specifies the
Windows device to deploy and launch the UWP app on when using Build and Run
from the Editor.  
[WSABuildType](WSABuildType.html)| Build configurations for Windows Store
Visual Studio solutions.  
[WSAUWPBuildType](WSAUWPBuildType.html)| Determines the output build type when
building to Universal Windows Platform.  
[XboxBuildSubtarget](XboxBuildSubtarget.html)| Target Xbox build type.  
[XcodeBuildConfig](XcodeBuildConfig.html)| Build configurations for the Xcode
project Unity generates.  
  
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

