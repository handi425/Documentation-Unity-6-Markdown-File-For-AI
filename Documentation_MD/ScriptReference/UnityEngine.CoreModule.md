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

# UnityEngine.CoreModule

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

The Core module implements basic classes required for Unity to function.

This module cannot be disabled.

### Classes

[AddComponentMenu](AddComponentMenu.html)| The AddComponentMenu attribute
allows you to place a script anywhere in the "Component" menu, instead of just
the "Component->Scripts" menu.  
---|---  
[AlwaysLinkAssemblyAttribute](Scripting.AlwaysLinkAssemblyAttribute.html)|
Ensure an assembly is always processed during managed code stripping.  
[AnimationCurve](AnimationCurve.html)| Store a collection of Keyframes that
can be evaluated over time.  
[Application](Application.html)| Provides access to application runtime data.  
[Application](WSA.Application.html)| Provides essential methods related to
Window Store application.  
[Application](Device.Application.html)| Access to platform-specific
application runtime data.  
[ArchiveFileInterface](Unity.IO.Archive.ArchiveFileInterface.html)| Provides
methods for managing Unity archive files.  
[Arguments](DedicatedServer.Arguments.html)| DedicatedServer.Arguments
provides accessors for common CLI options  
[AssemblyIsEditorAssembly](AssemblyIsEditorAssembly.html)| Assembly level
attribute. Any classes in an assembly with this attribute will be considered
to be Editor Classes.  
[Assert](Assertions.Assert.html)| The Assert class contains assertion methods
for setting invariants in the code.  
[AssertionException](Assertions.AssertionException.html)| An exception that is
thrown when an assertion fails.  
[AsyncGPUReadback](Rendering.AsyncGPUReadback.html)| Allows the asynchronous
read back of GPU resources.  
[AsyncInstantiateOperation](AsyncInstantiateOperation.html)| Asynchronous
instantiate operation on UnityEngine.Object type.  
[AsyncInstantiateOperation<T0>](AsyncInstantiateOperation_1.html)| Provides a
generic method to instantiate operations asynchronously on a
UnityEngine.Object.  
[AsyncOperation](AsyncOperation.html)| Asynchronous operation coroutine.  
[AsyncReadManager](Unity.IO.LowLevel.Unsafe.AsyncReadManager.html)| With the
AsyncReadManager, you can perform asynchronous I/O operations through Unity's
virtual file system. You can perform these operations on any thread or job.  
[AsyncReadManagerMetrics](Unity.IO.LowLevel.Unsafe.AsyncReadManagerMetrics.html)|
Manages the recording and retrieval of metrics from the AsyncReadManager.  
[AsyncReadManagerMetricsFilters](Unity.IO.LowLevel.Unsafe.AsyncReadManagerMetricsFilters.html)|
Defines a filter for selecting specific categories of data when summarizing
AsyncReadManager metrics.  
[AsyncReadManagerSummaryMetrics](Unity.IO.LowLevel.Unsafe.AsyncReadManagerSummaryMetrics.html)|
A summary of the metrics collected for AsyncReadManager read operations.  
[Awaitable](Awaitable.html)| Custom Unity type that can be awaited and used as
an async return type in the C# asynchronous programming model.  
[Awaitable<T0>](Awaitable_1.html)| Custom Unity type that can be awaited and
used as an async return type in the C# asynchronous programming model.  
[AwaitableCompletionSource](AwaitableCompletionSource.html)| Objects allowing
to control completion of an Awaitable object from user code.  
[AwaitableCompletionSource<T0>](AwaitableCompletionSource_1.html)| Objects
allowing to control completion of an Awaitable object from user code.  
[BatchRendererGroup](Rendering.BatchRendererGroup.html)| A BatchRendererGroup
is an object that lets you perform customizable high performance rendering.  
[BeforeRenderOrderAttribute](BeforeRenderOrderAttribute.html)| Use this
BeforeRenderOrderAttribute when you need to specify a custom callback order
for Application.onBeforeRender.  
[Behaviour](Behaviour.html)| Behaviours are Components that can be enabled or
disabled.  
[BillboardAsset](BillboardAsset.html)| BillboardAsset describes how a
billboard is rendered.  
[BillboardRenderer](BillboardRenderer.html)| Renders a billboard from a
BillboardAsset.  
[BurstAuthorizedExternalMethodAttribute](Unity.Burst.BurstAuthorizedExternalMethodAttribute.html)|
The BurstAuthorizedExternalMethod attribute lets you mark a function as being
authorized for Burst to call from within a static constructor.  
[BurstDiscardAttribute](Unity.Burst.BurstDiscardAttribute.html)| The
BurstDiscard attribute lets you remove a method or property from being
compiled to native code by the burst compiler.  
[Caching](Caching.html)| The Caching class lets you manage cached
AssetBundles, downloaded using UnityWebRequestAssetBundle.GetAssetBundle.  
[Camera](Camera.html)| A Camera is a device through which the player views the
world.  
[CategoryInfoAttribute](Categorization.CategoryInfoAttribute.html)| Provide a
information to order and categorize at category level.  
[CollectionPool<T0,T1>](Pool.CollectionPool_2.html)| A Collection such as
List, HashSet, Dictionary etc can be pooled and reused by using a
CollectionPool.  
[ColorGamutUtility](ColorGamutUtility.html)| Utility class to query properties
of a ColorGamut.  
[ColorUsageAttribute](ColorUsageAttribute.html)| Attribute used to configure
the usage of the ColorField and Color Picker for a color.  
[ColorUtility](ColorUtility.html)| A collection of common color functions.  
[CommandBuffer](Rendering.CommandBuffer.html)| List of graphics commands to
execute.  
[CommandBufferExtensions](Rendering.CommandBufferExtensions.html)| Static
class providing extension methods for CommandBuffer.  
[Component](Component.html)| Base class for everything attached to a
GameObject.  
[ComputeBuffer](ComputeBuffer.html)| GPU data buffer, mostly for use with
compute shaders.  
[ComputeShader](ComputeShader.html)| Compute Shader asset.  
[ContextMenu](ContextMenu.html)| Use the ContextMenu attribute to add commands
to the context menu of the Inspector window.  
[ContextMenuItemAttribute](ContextMenuItemAttribute.html)| Use this attribute
to add a context menu to a field that calls a named method.  
[Coroutine](Coroutine.html)|  MonoBehaviour.StartCoroutine returns a
Coroutine. Instances of this class are only used to reference these
coroutines, and do not hold any exposed properties or functions.  
[Coverage](TestTools.Coverage.html)| Describes the interface for the code
coverage data exposed by mono.  
[CrashReport](CrashReport.html)| Holds data for a single application crash
event and provides access to all gathered crash reports.  
[CrashReporting](Windows.CrashReporting.html)| Exposes useful information
related to crash reporting on Windows platforms.  
[CreateAssetMenuAttribute](CreateAssetMenuAttribute.html)| Mark a
ScriptableObject-derived type to be automatically listed in the Assets/Create
submenu, so that instances of the type can be easily created and stored in the
project as ".asset" files.  
[Crypto](Windows.Crypto.html)| Class representing cryptography algorithms.  
[Cubemap](Cubemap.html)| Class for handling cube maps, Use this to create or
modify existing cube map assets.  
[CubemapArray](CubemapArray.html)| Class for handling Cubemap arrays.  
[CullingGroup](CullingGroup.html)| Describes a set of bounding spheres that
should have their visibility and distances maintained.  
[Cursor](Cursor.html)| Cursor API for setting the cursor (mouse pointer).  
[Cursor](WSA.Cursor.html)| Cursor API for Windows Store Apps.  
[CustomRenderTexture](CustomRenderTexture.html)| Custom Render Textures are an
extension to Render Textures that allow you to render directly to the Texture
using a Shader.  
[CustomRenderTextureManager](CustomRenderTextureManager.html)| Custom Render
Texture Manager.  
[CustomSampler](Profiling.CustomSampler.html)| Custom CPU Profiler label used
for profiling arbitrary code blocks.  
[CustomYieldInstruction](CustomYieldInstruction.html)| Base class for custom
yield instructions to suspend coroutines.  
[DataUtility](Sprites.DataUtility.html)| Helper utilities for accessing Sprite
data.  
[DeallocateOnJobCompletionAttribute](Unity.Collections.DeallocateOnJobCompletionAttribute.html)|
Automatically deallocates a native container when a job is finished.  
[Debug](Debug.html)| Class containing methods to ease debugging while
developing a game.  
[DefaultExecutionOrder](DefaultExecutionOrder.html)| Specifies the script
execution order for a MonoBehaviour-derived class relative to other
MonoBehaviour-derived types.  
[DelayedAttribute](DelayedAttribute.html)| Attribute used to make a float,
int, or string variable in a script be delayed.  
[Device](tvOS.Device.html)| Interface into tvOS specific functionality.  
[Device](iOS.Device.html)| Interface into iOS specific functionality.  
[DictationRecognizer](Windows.Speech.DictationRecognizer.html)|
DictationRecognizer listens to speech input and attempts to determine what
phrase was uttered.  
[DictionaryPool<T0,T1>](Pool.DictionaryPool_2.html)| A version of
CollectionPool<T0,T1> for Dictionaries.  
[Directory](Windows.Directory.html)| Exposes static methods for directory
operations.  
[DisallowMultipleComponent](DisallowMultipleComponent.html)| Prevents
MonoBehaviour of same type (or subtype) to be added more than once to a
GameObject.  
[DiscreteTimeTimeExtensions](Unity.IntegerTime.DiscreteTimeTimeExtensions.html)|
Extension methods for the DiscreteTime.  
[Display](Display.html)| Provides access to a display / screen for rendering
operations.  
[DisposeSentinel](Unity.Collections.LowLevel.Unsafe.DisposeSentinel.html)|
Contains methods that automatically detect memory leaks.  
[DynamicGI](DynamicGI.html)| Allows to control the dynamic Global
Illumination.  
[ElementInfoAttribute](Categorization.ElementInfoAttribute.html)| Provide a
information to order and categorize at element level (in a category).  
[EnumButtonsAttribute](EnumButtonsAttribute.html)| Attribute to enable editing
an enum with a ToggleButtonGroup.  
[ExcludeFromCoverageAttribute](TestTools.ExcludeFromCoverageAttribute.html)|
Allows you to exclude an Assembly, Class, Constructor, Method or Struct from
Coverage.  
[ExcludeFromObjectFactoryAttribute](ExcludeFromObjectFactoryAttribute.html)|
Add this attribute to a class to prevent the class and its inherited classes
from being created with ObjectFactory methods.  
[ExcludeFromPresetAttribute](ExcludeFromPresetAttribute.html)| Add this
attribute to a class to prevent creating a Preset from the instances of the
class.  
[ExecuteAlways](ExecuteAlways.html)| Causes a MonoBehaviour-derived class to
execute in Edit mode and prefab editing mode in addition to at runtime.  
[ExecuteInEditMode](ExecuteInEditMode.html)| Causes a MonoBehaviour-derived
class to execute in Edit mode in addition to at runtime.  
[ExpressionEvaluator](ExpressionEvaluator.html)| Evaluates simple math
expressions; supports int / float and operators: + - * / % ^ ( ).  
[ExternalGPUProfiler](Experimental.Rendering.ExternalGPUProfiler.html)| The
ExternalGPUProfiler API allows developers to programatically take GPU frame
captures in conjunction with supported external GPU profilers. GPU frame
captures can be used to both analyze performance and debug graphics related
issues.  
[File](Windows.File.html)| Provides static methods for file operations.  
[Flare](Flare.html)| A flare asset. Read more about flares in the components
reference.  
[FlareLayer](FlareLayer.html)| FlareLayer component.  
[FloatComparer](Assertions.Comparers.FloatComparer.html)| A float comparer
used by Assert performing approximate comparison.  
[FormerlySerializedAsAttribute](Serialization.FormerlySerializedAsAttribute.html)|
Use this attribute to rename a field without losing its serialized value.  
[FrameCapture](Apple.FrameCapture.html)| Interface to control XCode Frame
Capture.  
[FrameDebugger](FrameDebugger.html)| Controls the Frame Debugger from a
script.  
[FrameTimingManager](FrameTimingManager.html)| The FrameTimingManager allows
the user to capture and access FrameTiming data for multiple frames.  
[GameObject](GameObject.html)| Base class for all objects that can exist in a
scene. Add components to a GameObject to control its appearance and behavior.  
[GarbageCollector](Scripting.GarbageCollector.html)| API to control the
garbage collector on the Mono and IL2CPP scripting backends.  
[GenericPool<T0>](Pool.GenericPool_1.html)| Provides a static implementation
of ObjectPool<T0>.  
[GeometryUtility](GeometryUtility.html)| Utility class for common geometric
functions.  
[Gizmos](Gizmos.html)| Gizmos are used to give visual debugging or setup aids
in the Scene view.  
[GL](GL.html)| Low-level graphics library.  
[Gradient](Gradient.html)| Represents a Gradient used for animating colors.  
[GradientUsageAttribute](GradientUsageAttribute.html)| Controls how the
Gradient inspector editor treats the color values.  
[GrammarRecognizer](Windows.Speech.GrammarRecognizer.html)| The
GrammarRecognizer is a complement to the KeywordRecognizer. In many cases
developers will find the KeywordRecognizer fills all their development needs.
However, in some cases, more complex grammars will be better expressed in the
form of an xml file on disk. The GrammarRecognizer uses Extensible Markup
Language (XML) elements and attributes, as specified in the World Wide Web
Consortium (W3C) Speech Recognition Grammar Specification (SRGS) Version 1.0.
These XML elements and attributes represent the rule structures that define
the words or phrases (commands) recognized by speech recognition engines.  
[Graphics](Graphics.html)| Raw interface to Unity's drawing functions.  
[GraphicsBuffer](GraphicsBuffer.html)| GPU graphics data buffer, for working
with geometry or compute shader data.  
[GraphicsFormatUtility](Experimental.Rendering.GraphicsFormatUtility.html)|
This utility class contains helper functions that enable you to query
properties of a TextureFormat, RenderTextureFormat, or GraphicsFormat. This
class also includes format conversion and size calculation functions.  
[GraphicsSettings](Rendering.GraphicsSettings.html)| Script interface for
Graphics Settings.  
[GraphicsStateCollection](Experimental.Rendering.GraphicsStateCollection.html)|
Collection of shader variants and associated graphics states.  
[GraphicsTexture](Rendering.GraphicsTexture.html)| Represents the view on a
single texture resource that is uploaded to the graphics device.  
[Handheld](Handheld.html)| Interface into functionality unique to handheld
devices.  
[HashSetPool<T0>](Pool.HashSetPool_1.html)| A version of CollectionPool<T0,T1>
for HashSets.  
[HashUnsafeUtilities](HashUnsafeUtilities.html)| Utilities to compute hashes
with unsafe code.  
[HashUtilities](HashUtilities.html)| Utilities to compute hashes.  
[HDROutputSettings](HDROutputSettings.html)| Provides access to HDR display
settings and information.  
[HeaderAttribute](HeaderAttribute.html)| Use this PropertyAttribute to add a
header above some fields in the Inspector.  
[HelpURLAttribute](HelpURLAttribute.html)| Provide a custom documentation URL
for a class.  
[HideInCallstackAttribute](HideInCallstackAttribute.html)| Marks the methods
you want to hide from the Console window callstack. When you hide these
methods they are removed from the detail area of the selected message in the
Console window.  
[HideInInspector](HideInInspector.html)| Flags a variable to not appear in the
Inspector.  
[IconAttribute](IconAttribute.html)| Attribute to specify an icon for a
MonoBehaviour or ScriptableObject.  
[IgnoredByDeepProfilerAttribute](Unity.Profiling.IgnoredByDeepProfilerAttribute.html)|
IgnoredByDeepProfilerAttribute prevents Unity Profiler from capturing method
calls.  
[IJobExtensions](Unity.Jobs.IJobExtensions.html)| Contains extension methods
for jobs using the IJob interface.  
[IJobForExtensions](Unity.Jobs.IJobForExtensions.html)| Contains extension
methods for IJobFor job types.  
[IJobParallelForExtensions](Unity.Jobs.IJobParallelForExtensions.html)|
Contains extension methods for IJobParallelFor job types.  
[IJobParallelForTransformExtensions](Jobs.IJobParallelForTransformExtensions.html)|
Contains extension methods for IJobParallelForTransform.  
[ImageEffectAfterScale](ImageEffectAfterScale.html)| Any Image Effect with
this attribute will be rendered after Dynamic Resolution stage.  
[ImageEffectAllowedInSceneView](ImageEffectAllowedInSceneView.html)| Any Image
Effect with this attribute can be rendered into the Scene view camera.  
[ImageEffectOpaque](ImageEffectOpaque.html)| Any Image Effect with this
attribute will be rendered after opaque geometry but before transparent
geometry.  
[ImageEffectTransformsToLDR](ImageEffectTransformsToLDR.html)| When using HDR
rendering it can sometime be desirable to switch to LDR rendering during
ImageEffect rendering.  
[ImageEffectUsesCommandBuffer](ImageEffectUsesCommandBuffer.html)| Use this
attribute when image effects are implemented using Command Buffers.  
[Input](Windows.Input.html)| Provides static methods for Windows specific
input manipulation.  
[InspectorNameAttribute](InspectorNameAttribute.html)| Use this attribute on
enum value declarations to change the display name shown in the Inspector.  
[InspectorOrderAttribute](InspectorOrderAttribute.html)| Shows sorted enum
values in the Inspector enum UI dropdowns i.e. EditorGUI.EnumPopup,
PropertyField etc. This attribute can be applied to enum types only.  
[InvalidImportException](Rendering.InvalidImportException.html)| Exception
raised by the Resource Loader on SRP's.  
[JobHandleUnsafeUtility](Unity.Jobs.LowLevel.Unsafe.JobHandleUnsafeUtility.html)|
Contains unsafe utility methods for JobHandle instances.  
[JobProducerTypeAttribute](Unity.Jobs.LowLevel.Unsafe.JobProducerTypeAttribute.html)|
Indicates that a job interface's Execute method can be Burst compiled.  
[JobsUtility](Unity.Jobs.LowLevel.Unsafe.JobsUtility.html)| Provides methods
for creating, running, and debugging jobs.  
[KeywordRecognizer](Windows.Speech.KeywordRecognizer.html)| KeywordRecognizer
listens to speech input and attempts to match uttered phrases to a list of
registered keywords.  
[Launcher](WSA.Launcher.html)| Class which is capable of launching user's
default app for file type or a protocol. See also PlayerSettings where you can
specify file or URI associations.  
[LensFlare](LensFlare.html)| Script interface for a Lens flare component.  
[LicenseInformation](Windows.LicenseInformation.html)| This class provides
information regarding application's trial status and allows initiating
application purchase.  
[Light](Light.html)| Script interface for light components.  
[Light2DBase](U2D.Light2DBase.html)| Provides a base class for 2D lights.  
[LightingSettings](LightingSettings.html)| An object containing settings for
precomputing lighting data, that Unity can serialize as a Lighting Settings
Asset.  
[LightmapData](LightmapData.html)| Data of a lightmap.  
[LightmapperUtils](Experimental.GlobalIllumination.LightmapperUtils.html)|
Utility class for converting Unity Lights to light types recognized by the
baking backends.  
[Lightmapping](Experimental.GlobalIllumination.Lightmapping.html)| Interface
to the light baking backends.  
[LightmapSettings](LightmapSettings.html)| Stores lightmaps of the Scene.  
[LightProbeGroup](LightProbeGroup.html)| Light Probe Group.  
[LightProbeProxyVolume](LightProbeProxyVolume.html)| The Light Probe Proxy
Volume component offers the possibility to use higher resolution lighting for
large non-static GameObjects.  
[LightProbes](LightProbes.html)| Stores light probe data for all currently
loaded Scenes.  
[LineRenderer](LineRenderer.html)| The line renderer is used to draw free-
floating lines in 3D space.  
[LineUtility](LineUtility.html)| A collection of common line functions.  
[LinkedPool<T0>](Pool.LinkedPool_1.html)| A linked list version of
IObjectPool<T0>.  
[ListPool<T0>](Pool.ListPool_1.html)| A version of CollectionPool<T0,T1> for
Lists.  
[LoadStoreActionDebugModeSettings](Rendering.LoadStoreActionDebugModeSettings.html)|
Whether to show undefined areas of the display that might cause rendering
problems in your built application.  
[LODGroup](LODGroup.html)| LODGroup lets you group multiple Renderers into LOD
levels.  
[Logger](Logger.html)| Initializes a new instance of the Logger.  
[ManagedReferenceUtility](Serialization.ManagedReferenceUtility.html)| Utility
functions related to SerializeReference manipulation and access.  
[Material](Material.html)| The material class.  
[MaterialPropertyBlock](MaterialPropertyBlock.html)| A block of material
values to apply.  
[MemoryProfiler](Unity.Profiling.Memory.MemoryProfiler.html)| The memory
profiler API provides functionality for taking memory snapshots or adding
metadata to them.  
[MemorySnapshotMetadata](Unity.Profiling.Memory.MemorySnapshotMetadata.html)|
Container for memory snapshot metadata.  
[Mesh](Mesh.html)| A class that allows you to create or modify meshes.  
[MeshFilter](MeshFilter.html)| A class to access the Mesh of the mesh filter.  
[MeshRenderer](MeshRenderer.html)| Renders meshes inserted by the MeshFilter
or TextMesh.  
[MessageEventArgs](Networking.PlayerConnection.MessageEventArgs.html)|
Arguments passed to Action callbacks registered in PlayerConnection.  
[MinAttribute](MinAttribute.html)| Attribute used to make a float or int
variable in a script be restricted to a specific minimum value.  
[MonoBehaviour](MonoBehaviour.html)| MonoBehaviour is a base class that many
Unity scripts derive from.  
[MultilineAttribute](MultilineAttribute.html)| Attribute to make a string be
edited with a multi-line textfield.  
[NativeArrayUnsafeUtility](Unity.Collections.LowLevel.Unsafe.NativeArrayUnsafeUtility.html)|
Contains unsafe methods for working with NativeArray instances.  
[NativeContainerAttribute](Unity.Collections.LowLevel.Unsafe.NativeContainerAttribute.html)|
Allows you to create your own custom native container.  
[NativeContainerIsAtomicWriteOnlyAttribute](Unity.Collections.LowLevel.Unsafe.NativeContainerIsAtomicWriteOnlyAttribute.html)|
Indicates that the native container only allows writing, and can only be
written to in safe, parallel contexts.  
[NativeContainerIsReadOnlyAttribute](Unity.Collections.LowLevel.Unsafe.NativeContainerIsReadOnlyAttribute.html)|
Marks a native container type as read only.  
[NativeContainerSupportsDeallocateOnJobCompletionAttribute](Unity.Collections.LowLevel.Unsafe.NativeContainerSupportsDeallocateOnJobCompletionAttribute.html)|
Indicates that a NativeContainer can be automatically deallocated when a job
is complete.  
[NativeContainerSupportsDeferredConvertListToArray](Unity.Collections.LowLevel.Unsafe.NativeContainerSupportsDeferredConvertListToArray.html)|
Indicates that the native container type can be passed to the Schedule method
of an IJobParallelForDefer job.  
[NativeContainerSupportsMinMaxWriteRestrictionAttribute](Unity.Collections.LowLevel.Unsafe.NativeContainerSupportsMinMaxWriteRestrictionAttribute.html)|
Indicates that a native container type can restrict its writable ranges to be
between a min and a max index.  
[NativeDisableContainerSafetyRestrictionAttribute](Unity.Collections.LowLevel.Unsafe.NativeDisableContainerSafetyRestrictionAttribute.html)|
Explicitly disable the safety system for a NativeContainer.  
[NativeDisableParallelForRestrictionAttribute](Unity.Collections.NativeDisableParallelForRestrictionAttribute.html)|
Indicates that multiple jobs can safely access the same NativeContainer at the
same time.  
[NativeDisableUnsafePtrRestrictionAttribute](Unity.Collections.LowLevel.Unsafe.NativeDisableUnsafePtrRestrictionAttribute.html)|
Enable the use of unsafe pointers in jobs.  
[NativeFixedLengthAttribute](Unity.Collections.NativeFixedLengthAttribute.html)|
Indicates that a native container has a size that will never change.  
[NativeLeakDetection](Unity.Collections.NativeLeakDetection.html)| Contains
settings for native leak detection.  
[NativeSetClassTypeToNullOnScheduleAttribute](Unity.Collections.LowLevel.Unsafe.NativeSetClassTypeToNullOnScheduleAttribute.html)|
Sets the managed reference to a class to null on a copy of the job struct that
is passed to a job.  
[NativeSetThreadIndexAttribute](Unity.Collections.LowLevel.Unsafe.NativeSetThreadIndexAttribute.html)|
Inject a worker thread index into an int on the job struct.  
[NativeSliceUnsafeUtility](Unity.Collections.LowLevel.Unsafe.NativeSliceUnsafeUtility.html)|
Contains unsafe methods for working with NativeSlice instances.  
[NonReorderableAttribute](NonReorderableAttribute.html)| Disables reordering
of an array or list in the Inspector window.  
[Notification](Playables.Notification.html)| Default implementation for
Playable notifications.  
[Object](Object.html)| Base class for all objects Unity can reference.  
[ObjectIdRequest](Rendering.ObjectIdRequest.html)| ObjectId request that can
be used to determine the object corresponding to each pixel. Can be submitted
using either Camera.SubmitRenderRequest or RenderPipeline.SubmitRenderRequest,
and the results can be used either on the CPU in C# or the GPU in a shader.  
[ObjectIdResult](Rendering.ObjectIdResult.html)| The results of an
ObjectIdRequest, stored in ObjectIdRequest._result, containing the
ObjectIdResult.idToObjectMapping that is needed to interpret the color-encoded
object IDs that are rendered in the ObjectIdRequest._destination
RenderTexture.  
[ObjectPool<T0>](Pool.ObjectPool_1.html)| A stack based IObjectPool<T0>.  
[OcclusionArea](OcclusionArea.html)| OcclusionArea is an area in which
occlusion culling is performed.  
[OcclusionPortal](OcclusionPortal.html)| The portal for dynamically changing
occlusion at runtime.  
[OnDemandRendering](Rendering.OnDemandRendering.html)| Use the
OnDemandRendering class to control and query information about your
application's rendering speed independent from all other subsystems (such as
physics, input, or animation).  
[OnDemandResources](iOS.OnDemandResources.html)| On Demand Resources API.  
[OnDemandResourcesRequest](iOS.OnDemandResourcesRequest.html)| Represents a
request for On Demand Resources (ODR). It's an AsyncOperation and can be
yielded in a coroutine.  
[PhotoCapture](Windows.WebCam.PhotoCapture.html)| Captures a photo from the
web camera and stores it in memory or on disk.  
[PhotoCaptureFrame](Windows.WebCam.PhotoCaptureFrame.html)| Contains
information captured from the web camera.  
[PhraseRecognitionSystem](Windows.Speech.PhraseRecognitionSystem.html)| Phrase
recognition system is responsible for managing phrase recognizers and
dispatching recognition events to them.  
[PhraseRecognizer](Windows.Speech.PhraseRecognizer.html)| A common base class
for both keyword recognizer and grammar recognizer.  
[Ping](Ping.html)| Ping any given IP address (given in dot notation).  
[PIX](Rendering.PIX.html)| Provides an interface to control GPU frame capture
in Microsoft's PIX software.  
[PixelPerfectRendering](U2D.PixelPerfectRendering.html)| A collection of APIs
that facilitate pixel perfect rendering of sprite-based renderers.  
[PlayableAsset](Playables.PlayableAsset.html)| A base class for assets that
can be used to instantiate a Playable at runtime.  
[PlayableBehaviour](Playables.PlayableBehaviour.html)| PlayableBehaviour is
the base class from which every custom playable script derives.  
[PlayableExtensions](Playables.PlayableExtensions.html)| Extensions for all
the types that implements IPlayable.  
[PlayableOutputExtensions](Playables.PlayableOutputExtensions.html)|
Extensions for all the types that implements IPlayableOutput.  
[PlayerConnection](Networking.PlayerConnection.PlayerConnection.html)| Used
for handling the network connection from the Player to the Editor.  
[PlayerLoop](LowLevel.PlayerLoop.html)| The class representing the player loop
in Unity.  
[PlayerPrefs](PlayerPrefs.html)|  PlayerPrefs is a class that stores Player
preferences between game sessions. It can store string, float and integer
values into the user’s platform registry.  
[PlayerPrefsException](PlayerPrefsException.html)| An exception thrown by the
PlayerPrefs class in a web player build.  
[PreferBinarySerialization](PreferBinarySerialization.html)| Prefer
ScriptableObject derived type to use binary serialization regardless of
project's asset serialization mode.  
[PreserveAttribute](Scripting.PreserveAttribute.html)| PreserveAttribute
prevents byte code stripping from removing a class, method, field, or
property.  
[Profiler](Profiling.Profiler.html)| Controls the Profiler from script.  
[ProfilerUnsafeUtility](Unity.Profiling.LowLevel.Unsafe.ProfilerUnsafeUtility.html)|
Utility class which provides access to low level Profiler API.  
[Projector](Projector.html)| A script interface for a projector component.  
[PropertyAttribute](PropertyAttribute.html)| Base class to derive custom
property attributes from. Use this to create custom attributes for script
variables.  
[QualitySettings](QualitySettings.html)| This represents the script interface
for Quality Settings.  
[Random](Random.html)| Easily generate random data for games.  
[RangeAttribute](RangeAttribute.html)| Attribute used to make a float or int
variable in a script be restricted to a specific range.  
[RationalTimeExtensions](Unity.IntegerTime.RationalTimeExtensions.html)|
Extension method operations for RationalTime.  
[RayTracingAccelerationStructure](Rendering.RayTracingAccelerationStructure.html)|
A data structure used to represent the geometry in the Scene for GPU ray
tracing.  
[RayTracingShader](Rendering.RayTracingShader.html)| A shader for GPU ray
tracing.  
[ReadOnlyAttribute](Unity.Collections.ReadOnlyAttribute.html)| Marks a member
of a struct used in a job as read-only.  
[Recorder](Profiling.Recorder.html)| Records profiling data produced by a
specific Sampler.  
[RecreatePipelineOnChangeAttribute](Rendering.RecreatePipelineOnChangeAttribute.html)|
This attribute is used on field of a IRenderPipelineGraphicsSettings to ensure
pipeline would be recreated if the value is changed.  
[RectOffset](RectOffset.html)| Offsets for rectangles, borders, etc.  
[RectTransform](RectTransform.html)| Position, size, anchor and pivot
information for a rectangle.  
[ReflectionProbe](ReflectionProbe.html)| The reflection probe is used to
capture the surroundings into a texture which is passed to the shaders and
used for reflections.  
[Remote](tvOS.Remote.html)| A class for Apple TV remote input configuration.  
[Renderer](Renderer.html)| General functionality for all renderers.  
[RendererExtensions](RendererExtensions.html)| Extension methods to the
Renderer class, used only for the UpdateGIMaterials method used by the Global
Illumination System.  
[RenderPipeline](Rendering.RenderPipeline.html)| Defines a series of commands
and settings that describes how Unity renders a frame.  
[RenderPipelineAsset](Rendering.RenderPipelineAsset.html)| An asset that
produces a specific IRenderPipeline.  
[RenderPipelineAsset<T0>](Rendering.RenderPipelineAsset_1.html)| An asset that
produces a specific IRenderPipeline.  
[RenderPipelineGlobalSettings](Rendering.RenderPipelineGlobalSettings.html)| A
ScriptableObject to associate with a RenderPipeline and store project-wide
settings for that Pipeline.  
[RenderPipelineGraphicsSettingsCollection](Rendering.RenderPipelineGraphicsSettingsCollection.html)|
Container class for a list of IRenderPipelineGraphicsSettings objects.  
[RenderPipelineGraphicsSettingsExtensions](Rendering.RenderPipelineGraphicsSettingsExtensions.html)|
Class that contains extensions for  
[RenderPipelineManager](Rendering.RenderPipelineManager.html)| Render Pipeline
manager.  
[RenderSettings](Experimental.RenderSettings.html)| Experimental render
settings features.  
[RenderSettings](RenderSettings.html)| The Render Settings contain values for
a range of visual elements in your Scene, like fog and ambient light.  
[RenderSettings](Experimental.GlobalIllumination.RenderSettings.html)|
Experimental render settings features.  
[RenderTexture](RenderTexture.html)| Render textures are textures that can be
rendered to.  
[RequireAttributeUsagesAttribute](Scripting.RequireAttributeUsagesAttribute.html)|
Only allowed on attribute types. If the attribute type is marked, then so too
will all CustomAttributes of that type.  
[RequireComponent](RequireComponent.html)| The RequireComponent attribute
automatically adds required components as dependencies.  
[RequireDerivedAttribute](Scripting.RequireDerivedAttribute.html)| When the
type is marked, all types derived from that type will also be marked.  
[RequiredInterfaceAttribute](Scripting.RequiredInterfaceAttribute.html)| When
a type is marked, all interface implementations of the specified types will be
marked.  
[RequiredMemberAttribute](Scripting.RequiredMemberAttribute.html)| When a type
is marked, all of its members with [RequiredMember] are marked.  
[RequireImplementorsAttribute](Scripting.RequireImplementorsAttribute.html)|
When the interface type is marked, all types implementing that interface will
be marked.  
[ResourceFormattedPathsAttribute](Rendering.ResourceFormattedPathsAttribute.html)|
Attribute specifying information about the paths where these resources are
located.  
[ResourcePathAttribute](Rendering.ResourcePathAttribute.html)| This attribute
is used to describe what path to the asset should be used.  
[ResourcePathsAttribute](Rendering.ResourcePathsAttribute.html)| Attribute
specifying information about the paths where these resources are located.  
[ResourcePathsBaseAttribute](Rendering.ResourcePathsBaseAttribute.html)| This
abstract attribute is used to describe what path to the asset should be used.  
[ResourceRequest](ResourceRequest.html)| Asynchronous load request from the
Resources bundle.  
[Resources](Resources.html)| The Resources class allows you to find and access
Objects including assets.  
[ResourcesAPI](ResourcesAPI.html)| Derive from this base class to provide
alternative implementations to the C# behavior of specific Resources methods.  
[RuntimeInitializeOnLoadMethodAttribute](RuntimeInitializeOnLoadMethodAttribute.html)|
Use this attribute to get a callback when the runtime is starting up and
loading the first scene.  
[Sampler](Profiling.Sampler.html)| Provides control over a CPU Profiler label.  
[ScalableBufferManager](ScalableBufferManager.html)| Scales render textures to
support dynamic resolution if the target platform/graphics API supports it.  
[SceneManager](SceneManagement.SceneManager.html)| Scene management at run-
time.  
[SceneManagerAPI](SceneManagement.SceneManagerAPI.html)| Derive from this base
class to provide alternative implementations to the C# behavior of specific
SceneManager methods.  
[SceneUtility](SceneManagement.SceneUtility.html)| Scene and Build Settings
related utilities.  
[Screen](Screen.html)| Provides access to display information.  
[Screen](Device.Screen.html)| Access platform-specific display information.  
[ScriptableObject](ScriptableObject.html)| A class you can derive from if you
want to create objects that live independently of GameObjects.  
[ScriptableRuntimeReflectionSystem](Experimental.Rendering.ScriptableRuntimeReflectionSystem.html)|
Empty implementation of IScriptableRuntimeReflectionSystem.  
[ScriptableRuntimeReflectionSystemSettings](Experimental.Rendering.ScriptableRuntimeReflectionSystemSettings.html)|
Global settings for the scriptable runtime reflection system.  
[ScriptPlayableBinding](Playables.ScriptPlayableBinding.html)| A
PlayableBinding that contains information representing a
ScriptingPlayableOutput.  
[SearchContextAttribute](Search.SearchContextAttribute.html)| This attribute
can be attached to a component object field in order to have the ObjectField
use the advanced Object Picker.  
[Security](Security.html)| Webplayer security related class. Not supported
from 5.4.0 onwards.  
[SelectionBaseAttribute](SelectionBaseAttribute.html)| Add this attribute to a
script class to mark its GameObject as a selection base object for Scene View
picking.  
[SerializeField](SerializeField.html)| Force Unity to serialize a private
field.  
[SerializeReference](SerializeReference.html)| A scripting attribute that
instructs Unity to serialize a field as a reference instead of as a value.  
[Shader](Shader.html)| Shader scripts used for all rendering.  
[ShaderVariantCollection](ShaderVariantCollection.html)|
ShaderVariantCollection records which shader variants are actually used in
each shader.  
[ShaderWarmup](Experimental.Rendering.ShaderWarmup.html)| Prewarms shaders in
a way that is supported by all graphics APIs.  
[SkinnedMeshRenderer](SkinnedMeshRenderer.html)| The Skinned Mesh filter.  
[Skybox](Skybox.html)| A script interface for the skybox component.  
[SleepTimeout](SleepTimeout.html)| Constants for special values of
Screen.sleepTimeout.  
[Snapping](Snapping.html)| Snap values to rounded increments.  
[SortingGroup](Rendering.SortingGroup.html)| Adding a SortingGroup component
to a GameObject will ensure that all Renderers within the GameObject's
descendants will be sorted and rendered together.  
[SpaceAttribute](SpaceAttribute.html)| Use this PropertyAttribute to add some
spacing in the Inspector.  
[SparseTexture](SparseTexture.html)| Class for handling Sparse Textures.  
[SplashScreen](Rendering.SplashScreen.html)| Provides an interface to the
Unity splash screen.  
[Sprite](Sprite.html)| Represents a Sprite object for use in 2D gameplay.  
[SpriteAtlas](U2D.SpriteAtlas.html)| Sprite Atlas is an asset created within
Unity. It is part of the built-in sprite packing solution.  
[SpriteAtlasManager](U2D.SpriteAtlasManager.html)| Manages SpriteAtlas during
runtime.  
[SpriteDataAccessExtensions](U2D.SpriteDataAccessExtensions.html)| A list of
methods designed for reading and writing to the rich internal data of a
Sprite.  
[SpriteRenderer](SpriteRenderer.html)| Renders a Sprite for 2D graphics.  
[SpriteRendererDataAccessExtensions](U2D.SpriteRendererDataAccessExtensions.html)|
A list of methods that allow the caller to override what the SpriteRenderer
renders.  
[StaticBatchingUtility](StaticBatchingUtility.html)| StaticBatchingUtility can
prepare your objects to take advantage of Unity's static batching.  
[SupportedOnRenderPipelineAttribute](Rendering.SupportedOnRenderPipelineAttribute.html)|
Set which render pipelines make a class active.  
[SupportedRenderingFeatures](Rendering.SupportedRenderingFeatures.html)|
Describes the rendering features supported by a given render pipeline.  
[SystemInfo](SystemInfo.html)| Access system and hardware information.  
[SystemInfo](Device.SystemInfo.html)| Access platform-specific system and
hardware information.  
[TextAreaAttribute](TextAreaAttribute.html)| Attribute to make a string be
edited with a height-flexible and scrollable text area.  
[TextAsset](TextAsset.html)| Represents a raw text or binary file asset.  
[Texture](Texture.html)| Base class for Texture handling.  
[Texture2D](Texture2D.html)| Class that represents textures in C# code.  
[Texture2DArray](Texture2DArray.html)| Class for handling 2D texture arrays.  
[Texture3D](Texture3D.html)| Class for handling 3D Textures, Use this to
create 3D texture assets.  
[TextureMipmapLimitGroups](TextureMipmapLimitGroups.html)| Script interface
for texture mipmap limit groups.  
[TexturePlayableBinding](Experimental.Playables.TexturePlayableBinding.html)|
A PlayableBinding that contains information representing a
TexturePlayableOutput.  
[Tile](WSA.Tile.html)| Represents tile on Windows start screen  
[Time](Time.html)| Provides an interface to get time information from Unity.  
[Toast](WSA.Toast.html)| Represents a toast notification in Windows Store
Apps.  
[TooltipAttribute](TooltipAttribute.html)| Specify a tooltip for a field in
the Inspector window.  
[TouchScreenKeyboard](TouchScreenKeyboard.html)| Interface for on-screen
keyboards. Only native iPhone, Android, and Windows Store Apps are supported.  
[TrailRenderer](TrailRenderer.html)| The trail renderer is used to make trails
behind objects in the Scene as they move about.  
[Transform](Transform.html)| Position, rotation and scale of an object.  
[UnityAPICompatibilityVersionAttribute](UnityAPICompatibilityVersionAttribute.html)|
Declares an assembly to be compatible (API wise) with a specific Unity API.
Used by internal tools to avoid processing the assembly in order to decide
whether assemblies may be using old Unity API.  
[UnityEvent](Events.UnityEvent.html)| A zero argument persistent callback that
can be saved with the Scene.  
[UnityEvent<T0,T1,T2,T3>](Events.UnityEvent_4.html)| Four argument version of
UnityEvent.  
[UnityEvent<T0,T1,T2>](Events.UnityEvent_3.html)| Three argument version of
UnityEvent.  
[UnityEvent<T0,T1>](Events.UnityEvent_2.html)| Two argument version of
UnityEvent.  
[UnityEvent<T0>](Events.UnityEvent_1.html)| One argument version of
UnityEvent.  
[UnityEventBase](Events.UnityEventBase.html)| Abstract base class for
UnityEvents.  
[UnsafeGenericPool<T0>](Pool.UnsafeGenericPool_1.html)| Provides a static
implementation of ObjectPool<T0>.  
[UnsafeUtility](Unity.Collections.LowLevel.Unsafe.UnsafeUtility.html)|
Contains unsafe utility methods.  
[Utils](Diagnostics.Utils.html)| A utility class that you can use for
diagnostic purposes.  
[VideoCapture](Windows.WebCam.VideoCapture.html)| Records a video from the web
camera directly to disk.  
[VirtualFileSystem](Unity.IO.LowLevel.Unsafe.VirtualFileSystem.html)| Class
that provides access to some of the Unity low level virtual file system APIs.  
[WaitForEndOfFrame](WaitForEndOfFrame.html)| Waits until the end of the frame
after Unity has rendered every Camera and GUI, just before displaying the
frame on screen.  
[WaitForFixedUpdate](WaitForFixedUpdate.html)| Waits until next fixed frame
rate update function. Additional resources: FixedUpdate.  
[WaitForSeconds](WaitForSeconds.html)| Suspends the coroutine execution for
the given amount of seconds using scaled time.  
[WaitForSecondsRealtime](WaitForSecondsRealtime.html)| Suspends the coroutine
execution for the given amount of seconds using unscaled time.  
[WaitUntil](WaitUntil.html)| Suspends the coroutine execution until the
supplied delegate evaluates to true.  
[WaitWhile](WaitWhile.html)| Suspends the coroutine execution until the
supplied delegate evaluates to false.  
[Watermark](Rendering.Watermark.html)| Provides an interface to the system
that draws the Unity trial version and development build watermarks in screen
space.  
[WebCam](Windows.WebCam.WebCam.html)| Contains general information about the
current state of the web camera.  
[WriteAccessRequiredAttribute](Unity.Collections.LowLevel.Unsafe.WriteAccessRequiredAttribute.html)|
Specify which struct method and property requires write access to be invoked.  
[WriteOnlyAttribute](Unity.Collections.WriteOnlyAttribute.html)| Marks a
member of a struct used in a job as write-only.  
[YieldInstruction](YieldInstruction.html)| Base class for all yield
instructions.  
  
### Structs

[ApplicationMemoryUsageChange](ApplicationMemoryUsageChange.html)| Contains
information about a change in the application's memory usage.  
---|---  
[ArchiveFileInfo](Unity.IO.Archive.ArchiveFileInfo.html)| Represents
information about a file included in an archive.  
[ArchiveHandle](Unity.IO.Archive.ArchiveHandle.html)| Represents an
asynchronous operation handle that references an archive.  
[AsyncGPUReadbackRequest](Rendering.AsyncGPUReadbackRequest.html)| Represents
an asynchronous request for a GPU resource.  
[AsyncReadManagerRequestMetric](Unity.IO.LowLevel.Unsafe.AsyncReadManagerRequestMetric.html)|
Metrics for an individual read request.  
[AtomicSafetyHandle](Unity.Collections.LowLevel.Unsafe.AtomicSafetyHandle.html)|
Coordinate safe access to native container memory inside the job system.  
[AttachmentDescriptor](Rendering.AttachmentDescriptor.html)| A declaration of
a single color or depth rendering surface to be attached into a RenderPass.  
[AttachmentIndexArray](Rendering.AttachmentIndexArray.html)| Struct
encapsulating a fixed list of attachment indices used when declaring native
render passes.  
[BatchCullingContext](Rendering.BatchCullingContext.html)| Culling context for
a batch.  
[BatchCullingOutput](Rendering.BatchCullingOutput.html)| Contains the output
data where OnPerformCulling will write draw commands into.  
[BatchCullingOutputDrawCommands](Rendering.BatchCullingOutputDrawCommands.html)|
Draw commands generated by the culling request.  
[BatchDrawCommand](Rendering.BatchDrawCommand.html)| Represents a draw command
for a BatchRendererGroup.  
[BatchDrawCommandIndirect](Rendering.BatchDrawCommandIndirect.html)|
Represents an indirect draw command for a BatchRendererGroup.  
[BatchDrawCommandProcedural](Rendering.BatchDrawCommandProcedural.html)|
Represents a procedural draw command for a BatchRendererGroup.  
[BatchDrawCommandProceduralIndirect](Rendering.BatchDrawCommandProceduralIndirect.html)|
Represents a procedural indirect draw command for a BatchRendererGroup.  
[BatchDrawRange](Rendering.BatchDrawRange.html)| Specifies a draw range of
draw commands.  
[BatchFilterSettings](Rendering.BatchFilterSettings.html)| Represents settings
that Unity applies to draw commands in this draw range.  
[BatchID](Rendering.BatchID.html)| The batch ID.  
[BatchMaterialID](Rendering.BatchMaterialID.html)| The batch Material ID.  
[BatchMeshID](Rendering.BatchMeshID.html)| The batch mesh ID.  
[BatchPackedCullingViewID](Rendering.BatchPackedCullingViewID.html)| The ID of
the view from which Unity invoked the culling.  
[BatchQueryJob<T0,T1>](Unity.Jobs.LowLevel.Unsafe.BatchQueryJob_2.html)|
Provides an implementation for batch query jobs.  
[BatchQueryJobStruct<T0>](Unity.Jobs.LowLevel.Unsafe.BatchQueryJobStruct_1.html)|
Provides an implementation for batch query jobs.  
[BatchRendererGroupCreateInfo](Rendering.BatchRendererGroupCreateInfo.html)|
Struct is used to initialize BatchRendererGroup.  
[BlendShapeBufferRange](BlendShapeBufferRange.html)| Describes the location of
blend shape vertex data in a GraphicsBuffer.  
[BlendState](Rendering.BlendState.html)| Values for the blend state.  
[BoneWeight](BoneWeight.html)| Describes 4 skinning bone weights that affect a
vertex in a mesh.  
[BoneWeight1](BoneWeight1.html)| Describes a bone weight that affects a vertex
in a mesh.  
[BoundingSphere](BoundingSphere.html)| Describes a single bounding sphere for
use by a CullingGroup.  
[Bounds](Bounds.html)| Represents an axis aligned bounding box.  
[BoundsInt](BoundsInt.html)| Represents an axis aligned bounding box with all
values as integers.  
[BuildCompression](BuildCompression.html)| Contains information about
compression methods, compression levels and block sizes that are supported by
Asset Bundle compression at build time and recompression at runtime.  
[Cache](Cache.html)| Data structure for cache. For more information, see
Caching.AddCache.  
[CachedAssetBundle](CachedAssetBundle.html)| Data structure for downloading
AssetBundles to a customized cache path. Additional
resources:UnityWebRequestAssetBundle.GetAssetBundle for more information.  
[CameraParameters](Windows.WebCam.CameraParameters.html)| When calling
PhotoCapture.StartPhotoModeAsync, you must pass in a CameraParameters object
that contains the various settings that the web camera will use.  
[CameraPlayable](Experimental.Playables.CameraPlayable.html)| An
implementation of IPlayable that produces a Camera texture.  
[CameraProperties](Rendering.CameraProperties.html)| Camera related properties
in CullingParameters.  
[Color](Color.html)| Representation of RGBA colors.  
[Color32](Color32.html)| Representation of RGBA colors in 32 bit format.  
[CombineInstance](CombineInstance.html)| Struct used to describe meshes to be
combined using Mesh.CombineMeshes.  
[ContentNamespace](Unity.Content.ContentNamespace.html)| Provides
functionality for grouping loaded Archive files into separate namespaces.  
[Cookie](Experimental.GlobalIllumination.Cookie.html)| A helper structure used
to initialize a LightDataGI structure with cookie information.  
[CoveredMethodStats](TestTools.CoveredMethodStats.html)| Describes the summary
of the code coverage for the specified method used by Coverage. For an example
of typical usage, see Coverage.GetStatsFor.  
[CoveredSequencePoint](TestTools.CoveredSequencePoint.html)| Describes a
covered sequence point used by Coverage. For an example of typical usage, see
Coverage.GetSequencePointsFor.  
[CreateSceneParameters](SceneManagement.CreateSceneParameters.html)| This
struct collects all the CreateScene parameters in to a single place.  
[CullingGroupEvent](CullingGroupEvent.html)| Provides information about the
current and previous states of one sphere in a CullingGroup.  
[CullingResults](Rendering.CullingResults.html)| A struct containing the
results of a culling operation.  
[CullingSplit](Rendering.CullingSplit.html)| This struct contains the
properties of a culling split.  
[CustomRenderTextureUpdateZone](CustomRenderTextureUpdateZone.html)| Structure
describing an Update Zone.  
[DebugScreenCapture](Unity.Profiling.DebugScreenCapture.html)| A raw data
representation of a screenshot.  
[DepthState](Rendering.DepthState.html)| Values for the depth state.  
[DirectionalLight](Experimental.GlobalIllumination.DirectionalLight.html)| A
helper structure used to initialize a LightDataGI structure as a directional
light.  
[DiscLight](Experimental.GlobalIllumination.DiscLight.html)| A helper
structure used to initialize a LightDataGI structure as a disc light.  
[DiscreteTime](Unity.IntegerTime.DiscreteTime.html)| Data-type representing a
discrete time value.  
[DisplayInfo](DisplayInfo.html)| Represents a connected display.  
[DrawingSettings](Rendering.DrawingSettings.html)| Settings for
ScriptableRenderContext.DrawRenderers.  
[DrivenRectTransformTracker](DrivenRectTransformTracker.html)| A component can
be designed to drive a RectTransform. The DrivenRectTransformTracker struct is
used to specify which RectTransforms it is driving.  
[EarlyUpdate](PlayerLoop.EarlyUpdate.html)| Update phase in the native player
loop.  
[ExposedPropertyResolver](ExposedPropertyResolver.html)| Object that is used
to resolve references to an ExposedReference field.  
[ExposedReference<T0>](ExposedReference_1.html)| Creates a type whos value is
resolvable at runtime.  
[FileHandle](Unity.IO.LowLevel.Unsafe.FileHandle.html)| A handle to an
asynchronously opened file.  
[FileInfoResult](Unity.IO.LowLevel.Unsafe.FileInfoResult.html)| The results of
an asynchronous AsyncReadManager.GetFileInfo call.  
[FilteringSettings](Rendering.FilteringSettings.html)| A struct that
represents filtering settings for ScriptableRenderContext.DrawRenderers.  
[FixedUpdate](PlayerLoop.FixedUpdate.html)| Update phase in the native player
loop.  
[FrameData](Playables.FrameData.html)| This structure contains the frame
information a Playable receives in Playable.PrepareFrame.  
[FrameTiming](FrameTiming.html)| Struct containing basic FrameTimings and
accompanying relevant data.  
[FrustumPlanes](FrustumPlanes.html)| This struct contains the view space
coordinates of the near projection plane.  
[GlobalKeyword](Rendering.GlobalKeyword.html)| Represents a global shader
keyword.  
[GradientAlphaKey](GradientAlphaKey.html)| Alpha key used by Gradient.  
[GradientColorKey](GradientColorKey.html)| Color key used by Gradient.  
[GraphicsBufferHandle](GraphicsBufferHandle.html)| Represents the internal
handle/id of a GraphicsBuffer.  
[GraphicsFence](Rendering.GraphicsFence.html)| Used to manage synchronisation
between tasks on async compute queues and the graphics queue.  
[GraphicsTextureDescriptor](Rendering.GraphicsTextureDescriptor.html)|
Contains all the information Unity uses to create a GraphicsTexture.  
[Hash128](Hash128.html)| Represents a 128-bit hash value.  
[Initialization](PlayerLoop.Initialization.html)| Update phase in the native
player loop.  
[InstantiateParameters](InstantiateParameters.html)| Parameters for
Object.Instantiate and Object.InstantiateAsync.  
[JobHandle](Unity.Jobs.JobHandle.html)| Represents a handle to a job, which
uniquely identifies a job scheduled in the job system.  
[JobRanges](Unity.Jobs.LowLevel.Unsafe.JobRanges.html)| Provides information
about a range that a job is allowed to work on.  
[Keyframe](Keyframe.html)| A single keyframe that can be injected into an
animation curve.  
[LayerMask](LayerMask.html)| Specifies Layers to use in a Physics.Raycast.  
[LazyLoadReference<T0>](LazyLoadReference_1.html)| Serializable lazy reference
to a UnityEngine.Object contained in an asset file.  
[LightBakingOutput](LightBakingOutput.html)| Struct describing the result of a
Global Illumination bake for a given light.  
[LightDataGI](Experimental.GlobalIllumination.LightDataGI.html)| The interop
structure to pass light information to the light baking backends. There are
helper structures for Directional, Point, Spot and Rectangle lights to
correctly initialize this structure.  
[LightProbesQuery](LightProbesQuery.html)| Thread-safe struct for batch
sampling Light Probes in a Scene.  
[LightShadowCasterCullingInfo](Rendering.LightShadowCasterCullingInfo.html)|
This structure contains the information to perform shadow caster culling for a
given light.  
[LinearColor](Experimental.GlobalIllumination.LinearColor.html)| Contains
normalized linear color values for red, green, blue in the range of 0 to 1,
and an additional intensity value.  
[LoadSceneParameters](SceneManagement.LoadSceneParameters.html)| This struct
collects all the LoadScene parameters in to a single place.  
[LocalKeyword](Rendering.LocalKeyword.html)| Represents a shader keyword
declared in a shader source file.  
[LocalKeywordSpace](Rendering.LocalKeywordSpace.html)| Represents the local
keyword space of a Shader or ComputeShader.  
[LOD](LOD.html)| Structure for building a LOD for passing to the SetLODs
function.  
[LODParameters](Rendering.LODParameters.html)|  LODGroup culling parameters.  
[MaterialEffectPlayable](Experimental.Playables.MaterialEffectPlayable.html)|
An implementation of IPlayable that allows application of a Material shader to
one or many texture inputs to produce a texture output.  
[Mathf](Mathf.html)| A collection of common math functions.  
[Matrix4x4](Matrix4x4.html)| A standard 4x4 transformation matrix.  
[MetadataValue](Rendering.MetadataValue.html)| Contains a single metadata
value for a batch.  
[MipmapLimitDescriptor](MipmapLimitDescriptor.html)| Determines whether a
texture uses a mipmap limit, and which mipmap limit the texture uses, when you
create the texture using a constructor.  
[NativeArray<T0>](Unity.Collections.NativeArray_1.html)| Provides a buffer of
native memory to managed code, making it possible to share data between
managed and native code without marshalling costs.  
[NativeSlice<T0>](Unity.Collections.NativeSlice_1.html)| Provides a view on a
buffer of native memory most commonly acquired from a NativeArray<T0>.  
[PassIdentifier](Rendering.PassIdentifier.html)| Represents an identifier of a
specific Pass in a Shader.  
[PhraseRecognizedEventArgs](Windows.Speech.PhraseRecognizedEventArgs.html)|
Provides information about a phrase recognized event.  
[Plane](Plane.html)| Representation of a plane in 3D space.  
[PlatformKeywordSet](Rendering.PlatformKeywordSet.html)| A collection of
ShaderKeyword that represents a specific platform variant.  
[Playable](Playables.Playable.html)| Playables are customizable runtime
objects that can be connected together and are contained in a PlayableGraph to
create complex behaviours.  
[PlayableBinding](Playables.PlayableBinding.html)| Struct that holds
information regarding an output of a PlayableAsset.  
[PlayableGraph](Playables.PlayableGraph.html)| Use the PlayableGraph to manage
Playable creations and destructions.  
[PlayableOutput](Playables.PlayableOutput.html)| See: IPlayableOutput.  
[PlayerLoopSystem](LowLevel.PlayerLoopSystem.html)| The representation of a
single system being updated by the player loop in Unity.  
[PointLight](Experimental.GlobalIllumination.PointLight.html)| A helper
structure used to initialize a LightDataGI structure as a point light.  
[PooledObject<T0>](Pool.PooledObject_1.html)|  A pooled object wraps a
reference to an instance returned to the pool when the pooled object is
disposed of.  
[Pose](Pose.html)| Representation of a Position, and a Rotation in 3D Space  
[PostLateUpdate](PlayerLoop.PostLateUpdate.html)| Update phase in the native
player loop.  
[PreLateUpdate](PlayerLoop.PreLateUpdate.html)| Update phase in the native
player loop.  
[PreUpdate](PlayerLoop.PreUpdate.html)| Update phase in the native player
loop.  
[ProfilerCategory](Unity.Profiling.ProfilerCategory.html)| Use to specify
category for instrumentation Profiler markers.  
[ProfilerCategoryDescription](Unity.Profiling.LowLevel.Unsafe.ProfilerCategoryDescription.html)|
Provides information about Profiler category.  
[ProfilerMarker](Unity.Profiling.ProfilerMarker.html)| Performance marker used
for profiling arbitrary code blocks.  
[ProfilerMarkerData](Unity.Profiling.LowLevel.Unsafe.ProfilerMarkerData.html)|
Describes Profiler metadata parameter that can be associated with a sample.  
[ProfilerRecorder](Unity.Profiling.ProfilerRecorder.html)| Records the
Profiler metric data that a Profiler marker or counter produces.  
[ProfilerRecorderDescription](Unity.Profiling.LowLevel.Unsafe.ProfilerRecorderDescription.html)|
Gets the description of a Profiler metric.  
[ProfilerRecorderHandle](Unity.Profiling.LowLevel.Unsafe.ProfilerRecorderHandle.html)|
Gets the handle of a Profiler metric.  
[ProfilerRecorderSample](Unity.Profiling.ProfilerRecorderSample.html)| Sample
value structure.  
[PropertyName](PropertyName.html)| Represents a string as an int for efficient
lookup and comparison. Use this for common PropertyNames.Internally stores
just an int to represent the string. A PropertyName can be created from a
string but can not be converted back to a string. The same string always
results in the same int representing that string. Thus this is a very
efficient string representation in both memory and speed when all you need is
comparison.PropertyName is serializable.ToString() is only implemented for
debugging purposes in the editor it returns "theName:3737" in the player it
returns "Unknown:3737".  
[Quaternion](Quaternion.html)| Quaternions are used to represent rotations.  
[RangeInt](RangeInt.html)| Describes an integer range.  
[RasterState](Rendering.RasterState.html)| Values for the raster state.  
[RationalTime](Unity.IntegerTime.RationalTime.html)| Data type that represents
time as an integer count of a rational number.  
[Ray](Ray.html)| Representation of rays.  
[Ray2D](Ray2D.html)| A ray in 2D space.  
[RayTracingAABBsInstanceConfig](Rendering.RayTracingAABBsInstanceConfig.html)|
The parameters you use to add an instance of ray tracing axis-aligned bounding
boxes (AABBs) to a RayTracingAccelerationStructure.  
[RayTracingGeometryInstanceConfig](Rendering.RayTracingGeometryInstanceConfig.html)|
Parameters you can use to configure ray tracing triangle geometry instances
that are part of a RayTracingAccelerationStructure.  
[RayTracingInstanceCullingConfig](Rendering.RayTracingInstanceCullingConfig.html)|
Parameters for culling and filtering ray tracing instances in
RayTracingAccelerationStructure.CullInstances.  
[RayTracingInstanceCullingMaterialTest](Rendering.RayTracingInstanceCullingMaterialTest.html)|
This structure is used by RayTracingAccelerationStructure.CullInstances
function to avoid adding Renderers to the acceleration structure or to ignore
individual sub-meshes in a Mesh based on Shaders used by Materials when
building the acceleration structure.  
[RayTracingInstanceCullingResults](Rendering.RayTracingInstanceCullingResults.html)|
A structure containing results of the culling operation performed by
RayTracingAccelerationStructure.CullInstances.  
[RayTracingInstanceCullingShaderTagConfig](Rendering.RayTracingInstanceCullingShaderTagConfig.html)|
A Shader Tag configuration used by
RayTracingAccelerationStructure.CullInstances to filter and classify
Materials.  
[RayTracingInstanceCullingTest](Rendering.RayTracingInstanceCullingTest.html)|
A testing configuration used in RayTracingAccelerationStructure.CullInstances
for adding Renderers to an acceleration structure based on their layer,
ShadowCastingMode and Material type.  
[RayTracingInstanceMaterialConfig](Rendering.RayTracingInstanceMaterialConfig.html)|
This structure is used by RayTracingAccelerationStructure.CullInstances
function to determine which types of Materials are used by Renderers when
populating the acceleration structure with ray tracing instances.  
[RayTracingInstanceMaterialCRC](Rendering.RayTracingInstanceMaterialCRC.html)|
A Material instance id and CRC hash value pair. This information is returned
by a RayTracingAccelerationStructure.CullInstances call.  
[RayTracingInstanceTriangleCullingConfig](Rendering.RayTracingInstanceTriangleCullingConfig.html)|
This structure is used by RayTracingAccelerationStructure.CullInstances
function to determine triangle culling and vertex winding order for ray
tracing instances.  
[RayTracingMeshInstanceConfig](Rendering.RayTracingMeshInstanceConfig.html)|
Parameters you can use to configure ray tracing Mesh instances that are part
of a RayTracingAccelerationStructure.  
[RayTracingSubMeshFlagsConfig](Rendering.RayTracingSubMeshFlagsConfig.html)| A
structure used by RayTracingAccelerationStructure.CullInstances that defines
the RayTracingSubMeshFlags values for different Material types.  
[ReadCommand](Unity.IO.LowLevel.Unsafe.ReadCommand.html)| Describes the
offset, size, and destination buffer of a single read operation.  
[ReadCommandArray](Unity.IO.LowLevel.Unsafe.ReadCommandArray.html)| An array
of ReadCommand instances to pass to AsyncReadManager.Read and
AsyncReadManager.ReadDeferred.  
[ReadHandle](Unity.IO.LowLevel.Unsafe.ReadHandle.html)| You can use this
handle to query the status of an asynchronous read operation. Note: To avoid a
memory leak, you must call Dispose.  
[Rect](Rect.html)| A 2D Rectangle defined by X and Y position, width and
height.  
[RectangleLight](Experimental.GlobalIllumination.RectangleLight.html)| A
helper structure used to initialize a LightDataGI structure as a rectangle
light.  
[RectInt](RectInt.html)| A 2D Rectangle defined by x, y, width, height with
integers.  
[ReflectionProbeBlendInfo](Rendering.ReflectionProbeBlendInfo.html)|
ReflectionProbeBlendInfo contains information required for blending probes.  
[RefreshRate](RefreshRate.html)| Represents the display refresh rate. This is
how many frames the display can show per second.  
[RenderBuffer](RenderBuffer.html)| Color or depth buffer part of a
RenderTexture.  
[RendererList](Rendering.RendererList.html)| Represents a set of visible
GameObjects.  
[RendererListDesc](Rendering.RendererUtils.RendererListDesc.html)| Represents
the set of GameObjects that a RendererList contains.  
[RendererListParams](Rendering.RendererListParams.html)| Struct holding the
arguments that are needed to create a renderers RendererList.  
[RenderingLayerMask](RenderingLayerMask.html)| The Render Pipeline allows you
to use Rendering Layers, which are LayerMasks to make Lights or effects only
affect specific Renderers.  
[RenderParams](RenderParams.html)| Rendering parameters used by various
rendering functions.  
[RenderQueueRange](Rendering.RenderQueueRange.html)| Describes a material
render queue range.  
[RenderStateBlock](Rendering.RenderStateBlock.html)| A set of values that
Unity uses to override the GPU's render state.  
[RenderTargetBinding](Rendering.RenderTargetBinding.html)| Describes a render
target with one or more color buffers, a depth/stencil buffer and the
associated load/store-actions that are applied when the render target is
active.  
[RenderTargetBlendState](Rendering.RenderTargetBlendState.html)| Values for
the blend state.  
[RenderTargetIdentifier](Rendering.RenderTargetIdentifier.html)| Identifies a
RenderTexture for a CommandBuffer.  
[RenderTargetSetup](RenderTargetSetup.html)| Fully describes setup of
RenderTarget.  
[RenderTextureDescriptor](RenderTextureDescriptor.html)| This struct contains
all the information required to create a RenderTexture. It can be copied,
cached, and reused to easily create RenderTextures that all share the same
properties. Avoid using the default constructor as it does not initialize some
flags with the recommended values.  
[Resolution](Resolution.html)| Represents a display resolution.  
[Scene](SceneManagement.Scene.html)| Run-time data structure for *.unity file.  
[ScopedRenderPass](Rendering.ScopedRenderPass.html)| Represents an active
render pass until disposed.  
[ScopedSubPass](Rendering.ScopedSubPass.html)| Represents an active sub pass
until disposed.  
[ScriptableCullingParameters](Rendering.ScriptableCullingParameters.html)|
Parameters that configure a culling operation in the Scriptable Render
Pipeline.  
[ScriptableRenderContext](Rendering.ScriptableRenderContext.html)| Defines
state and drawing commands that custom render pipelines use.  
[ScriptPlayable<T0>](Playables.ScriptPlayable_1.html)| A IPlayable
implementation that contains a PlayableBehaviour for the PlayableGraph.
PlayableBehaviour can be used to write custom Playable that implement their
own PrepareFrame callback.  
[ScriptPlayableOutput](Playables.ScriptPlayableOutput.html)| A IPlayableOutput
implementation that contains a script output for the a PlayableGraph.  
[SecondarySpriteTexture](SecondarySpriteTexture.html)| Encapsulates a
Texture2D and its shader property name to give Sprite-based renderers access
to a secondary texture, in addition to the main Sprite texture.  
[SecondaryTileData](WSA.SecondaryTileData.html)| Defines the default look of
secondary tile.  
[SemanticMeaning](Windows.Speech.SemanticMeaning.html)| Semantic meaning is a
collection of semantic properties of a recognized phrase. These semantic
properties can be specified in SRGS grammar files.  
[ShaderKeyword](Rendering.ShaderKeyword.html)| Represents an identifier for a
specific code path in a shader.  
[ShaderKeywordSet](Rendering.ShaderKeywordSet.html)| A collection of
ShaderKeyword that represents a specific shader variant.  
[ShaderTagId](Rendering.ShaderTagId.html)| Shader tag ids are used to refer to
various names in shaders.  
[ShaderWarmupSetup](Experimental.Rendering.ShaderWarmupSetup.html)| The
rendering configuration to use when prewarming shader variants.  
[ShadowCastersCullingInfos](Rendering.ShadowCastersCullingInfos.html)| This
structure contains the information to perform shadow casters culling for one
camera.  
[ShadowDrawingSettings](Rendering.ShadowDrawingSettings.html)| Settings for
ScriptableRenderContext.DrawShadows.  
[ShadowSplitData](Rendering.ShadowSplitData.html)| Describes the culling
information for a given shadow split (e.g. directional cascade).  
[SortingLayer](SortingLayer.html)| SortingLayer allows you to set the render
order of multiple sprites easily. There is always a default SortingLayer named
"Default" which all sprites are added to initially. Added more SortingLayers
to easily control the order of rendering of groups of sprites. Layers can be
ordered before or after the default layer.  
[SortingLayerRange](Rendering.SortingLayerRange.html)| Describes a renderer's
sorting layer range.  
[SortingSettings](Rendering.SortingSettings.html)| This struct describes the
methods to sort objects during rendering.  
[SphericalHarmonicsL2](Rendering.SphericalHarmonicsL2.html)| Spherical
harmonics up to the second order (3 bands, 9 coefficients).  
[SpotLight](Experimental.GlobalIllumination.SpotLight.html)| A helper
structure used to initialize a LightDataGI structure as a spot light.  
[SpotLightBoxShape](Experimental.GlobalIllumination.SpotLightBoxShape.html)|
Use this Struct to help initialize a LightDataGI structure as a box-shaped
spot light.  
[SpotLightPyramidShape](Experimental.GlobalIllumination.SpotLightPyramidShape.html)|
Use this Struct to help initialize a LightDataGI structure as a pyramid-shaped
spot light.  
[SpriteBone](U2D.SpriteBone.html)| Stores a set of information that describes
the bind pose of this Sprite.  
[StencilState](Rendering.StencilState.html)| Values for the stencil state.  
[SubMeshDescriptor](Rendering.SubMeshDescriptor.html)| Contains information
about a single sub-mesh of a Mesh.  
[SubPassDescriptor](Rendering.SubPassDescriptor.html)| Structure discribing a
single native subpass.  
[TagHandle](TagHandle.html)| A handle to one of the tag values that can be
applied to a GameObject.  
[TextureMipmapLimitSettings](TextureMipmapLimitSettings.html)| Structure that
represents texture mipmap limit settings.  
[TextureMixerPlayable](Experimental.Playables.TextureMixerPlayable.html)| An
implementation of IPlayable that allows mixing two textures.  
[TexturePlayableOutput](Experimental.Playables.TexturePlayableOutput.html)| An
IPlayableOutput implementation that will be used to manipulate textures.  
[ThreadedBatchContext](Rendering.ThreadedBatchContext.html)| Thread-safe and
Burst-safe API for interacting with a BatchRendererGroup from Burst jobs.  
[TimeUpdate](PlayerLoop.TimeUpdate.html)| Update phase in the native player
loop that waits for the operating system (OS) to flip the back buffer to the
display and update the time in the engine.  
[TransformAccess](Jobs.TransformAccess.html)| Represents the position,
rotation and scale of an object.  
[TransformAccessArray](Jobs.TransformAccessArray.html)| TransformAccessArray.  
[Update](PlayerLoop.Update.html)| Update phase in the native player loop.  
[Vector2](Vector2.html)| Representation of 2D vectors and points.  
[Vector2Int](Vector2Int.html)| Representation of 2D vectors and points using
integers.  
[Vector3](Vector3.html)| Representation of 3D vectors and points.  
[Vector3Int](Vector3Int.html)| Representation of 3D vectors and points using
integers.  
[Vector4](Vector4.html)| Representation of four-dimensional vectors.  
[VertexAttributeDescriptor](Rendering.VertexAttributeDescriptor.html)|
Information about a single VertexAttribute of a Mesh vertex.  
[VisibleLight](Rendering.VisibleLight.html)| Holds data of a visible light.  
[VisibleReflectionProbe](Rendering.VisibleReflectionProbe.html)| Holds data of
a visible reflection reflectionProbe.  
  
### Enumerations

[ActivityIndicatorStyle](iOS.ActivityIndicatorStyle.html)| ActivityIndicator
Style (iOS Specific).  
---|---  
[Allocator](Unity.Collections.Allocator.html)| Sets which allocation type to
use for a NativeArray.  
[AmbientMode](Rendering.AmbientMode.html)| Ambient lighting mode.  
[AndroidActivityIndicatorStyle](AndroidActivityIndicatorStyle.html)|
ActivityIndicator Style (Android Specific).  
[AngularFalloffType](Experimental.GlobalIllumination.AngularFalloffType.html)|
Sets the method to use to compute the angular attenuation of spot lights.  
[AnisotropicFiltering](AnisotropicFiltering.html)| Anisotropic filtering mode.  
[ApplicationInstallMode](ApplicationInstallMode.html)| Application
installation mode (Read Only).  
[ApplicationMemoryUsage](ApplicationMemoryUsage.html)| Describes the
application memory usage level.  
[ApplicationSandboxType](ApplicationSandboxType.html)| Application sandbox
type.  
[ArchiveStatus](Unity.IO.Archive.ArchiveStatus.html)| Options for tracking the
status of the archive operation.  
[AssetLoadingSubsystem](Unity.IO.LowLevel.Unsafe.AssetLoadingSubsystem.html)|
Subsystem tags for the read request, describing broad asset type or subsystem
that triggered the read request.  
[AtomicSafetyErrorType](Unity.Collections.LowLevel.Unsafe.AtomicSafetyErrorType.html)|
Error code for errors related to accessing native container instances in
different situations.  
[AudioType](AudioType.html)| Type of the imported(native) data.  
[BatchBufferTarget](Rendering.BatchBufferTarget.html)| Expected target for the
buffer passed to BatchRendererGroup.AddBatch.  
[BatchCullingFlags](Rendering.BatchCullingFlags.html)| Additional parameters
for the current culling context  
[BatchCullingProjectionType](Rendering.BatchCullingProjectionType.html)| The
projection type of a view that is being culled.  
[BatchCullingViewType](Rendering.BatchCullingViewType.html)| The type of an
object that is requesting culling.  
[BatchDrawCommandFlags](Rendering.BatchDrawCommandFlags.html)| Rendering
options for the BatchDrawCommand struct.  
[BatchDrawCommandType](Rendering.BatchDrawCommandType.html)| Enumerates the
different draw command types a BatchRendererGroup can draw.  
[BatteryStatus](BatteryStatus.html)| Enumeration for SystemInfo.batteryStatus
which represents the current status of the device's battery.  
[BlendMode](Rendering.BlendMode.html)| Blend mode for controlling the
blending.  
[BlendOp](Rendering.BlendOp.html)| Blend operation.  
[BlendShapeBufferLayout](Rendering.BlendShapeBufferLayout.html)| Determines
the data that Unity returns when you call Mesh.GetBlendShapeBuffer.  
[BuiltinRenderTextureType](Rendering.BuiltinRenderTextureType.html)| Built-in
temporary render textures produced during camera's rendering.  
[BuiltinShaderDefine](Rendering.BuiltinShaderDefine.html)| Defines set by
editor when compiling shaders, based on the target platform and GraphicsTier.  
[BuiltinShaderMode](Rendering.BuiltinShaderMode.html)| Built-in shader modes
used by GraphicsSettings.  
[BuiltinShaderType](Rendering.BuiltinShaderType.html)| Built-in shader types
used by GraphicsSettings.  
[CameraClearFlags](CameraClearFlags.html)| Values for Camera.clearFlags,
determining what to clear when rendering a Camera.  
[CameraEvent](Rendering.CameraEvent.html)| Defines a place in camera's
rendering to attach CommandBuffer objects to.  
[CameraHDRMode](Rendering.CameraHDRMode.html)| The HDR mode to use for
rendering.  
[CameraLateLatchMatrixType](Rendering.CameraLateLatchMatrixType.html)| The
types of camera matrices that support late latching.  
[CameraType](CameraType.html)| Describes different types of camera.  
[CaptureFlags](Unity.Profiling.Memory.CaptureFlags.html)| Flags that specify
what kind of data to capture in a snapshot.  
[CapturePixelFormat](Windows.WebCam.CapturePixelFormat.html)| The encoded
image or video pixel format to use for PhotoCapture and VideoCapture.  
[ColorGamut](ColorGamut.html)| Represents a color gamut.  
[ColorPrimaries](ColorPrimaries.html)| Represents a color space based on its
set of red, green, and blue color primaries.  
[ColorSpace](ColorSpace.html)| Color space for player settings.  
[ColorWriteMask](Rendering.ColorWriteMask.html)| Specifies which color
components will get written into the target framebuffer.  
[CommandBufferExecutionFlags](Rendering.CommandBufferExecutionFlags.html)|
Flags describing the intention for how the command buffer will be executed.
Set these via CommandBuffer.SetExecutionFlags.  
[CompareFunction](Rendering.CompareFunction.html)| Depth or stencil comparison
function.  
[CompressionLevel](CompressionLevel.html)| Compression Levels relate to how
much time should be spent compressing Assets into an Asset Bundle.  
[CompressionType](CompressionType.html)| Compression Method for Asset Bundles.  
[ComputeBufferMode](ComputeBufferMode.html)| Intended usage of the buffer.  
[ComputeBufferType](ComputeBufferType.html)|  ComputeBuffer type.  
[ComputeQueueType](Rendering.ComputeQueueType.html)| Describes the desired
characteristics with respect to prioritisation and load balancing of the queue
that a command buffer being submitted via Graphics.ExecuteCommandBufferAsync
or [[ScriptableRenderContext.ExecuteCommandBufferAsync] should be sent to.  
[ConfidenceLevel](Windows.Speech.ConfidenceLevel.html)| Used by
KeywordRecognizer, GrammarRecognizer, DictationRecognizer. Phrases under the
specified minimum level will be ignored.  
[ConnectionTarget](Networking.PlayerConnection.ConnectionTarget.html)| The
type of the connected target.  
[CopyTextureSupport](Rendering.CopyTextureSupport.html)| Support for various
Graphics.CopyTexture cases.  
[CubemapFace](CubemapFace.html)|  Cubemap face.  
[CullingOptions](Rendering.CullingOptions.html)| Flags used by
ScriptableCullingParameters.cullingOptions to configure a culling operation.  
[CullMode](Rendering.CullMode.html)| Determines which faces Unity culls.  
[CursorLockMode](CursorLockMode.html)| How the cursor should behave.  
[CursorMode](CursorMode.html)| Determines whether the mouse cursor is rendered
using software rendering or, on supported platforms, hardware rendering.  
[CustomMarkerCallbackFlags](Rendering.CustomMarkerCallbackFlags.html)| Flags
that determine what custom events get called when native plugin callback is
issued.  
[CustomRenderTextureInitializationSource](CustomRenderTextureInitializationSource.html)|
Specify the source of a Custom Render Texture initialization.  
[CustomRenderTextureUpdateMode](CustomRenderTextureUpdateMode.html)| Frequency
of update or initialization of a Custom Render Texture.  
[CustomRenderTextureUpdateZoneSpace](CustomRenderTextureUpdateZoneSpace.html)|
Space in which coordinates are provided for Update Zones.  
[DefaultFormat](Experimental.Rendering.DefaultFormat.html)|  Use a default
format to create either Textures or RenderTextures from scripts based on
platform specific capability.  
[DefaultReflectionMode](Rendering.DefaultReflectionMode.html)| Default
reflection mode.  
[DepthTextureMode](DepthTextureMode.html)| Depth texture generation mode for
Camera.  
[DeviceGeneration](tvOS.DeviceGeneration.html)| tvOS device generation.  
[DeviceGeneration](iOS.DeviceGeneration.html)| iOS device generation.  
[DeviceType](DeviceType.html)| Enumeration for SystemInfo.deviceType, denotes
a coarse grouping of kinds of devices.  
[DictationCompletionCause](Windows.Speech.DictationCompletionCause.html)|
Represents the reason why dictation session has completed.  
[DictationTopicConstraint](Windows.Speech.DictationTopicConstraint.html)|
DictationTopicConstraint enum specifies the scenario for which a specific
dictation recognizer should optimize.  
[DirectorUpdateMode](Playables.DirectorUpdateMode.html)| Defines what time
source is used to update a Director graph.  
[DirectorWrapMode](Playables.DirectorWrapMode.html)| Wrap mode for Playables.  
[DistanceMetric](Rendering.DistanceMetric.html)| Type of sorting to use while
rendering.  
[DrivenTransformProperties](DrivenTransformProperties.html)| An enumeration of
transform properties that can be driven on a RectTransform by an object.  
[EnforceJobResult](Unity.Collections.LowLevel.Unsafe.EnforceJobResult.html)|
Enumerates the possible values returned by AtomicSafetyHandle methods that
wait for all jobs accessing the native container associated with the handle to
finish.  
[FalloffType](Experimental.GlobalIllumination.FalloffType.html)| Available
falloff models for baking.  
[FastMemoryFlags](Rendering.FastMemoryFlags.html)| Control Fast Memory render
target layout.  
[FileReadType](Unity.IO.LowLevel.Unsafe.FileReadType.html)| The type of file
read requested from the AsyncReadManager.  
[FileState](Unity.IO.LowLevel.Unsafe.FileState.html)| Defines the possible
existential states of a file.  
[FileStatus](Unity.IO.LowLevel.Unsafe.FileStatus.html)| The possible statuses
of a FileHandle.  
[FilterMode](FilterMode.html)| Filtering mode for textures. Corresponds to the
settings in a texture inspector.  
[FindObjectsInactive](FindObjectsInactive.html)| Options to control whether
object find functions return inactive objects.  
[FindObjectsSortMode](FindObjectsSortMode.html)| Options to specify if and how
to sort objects returned by a function.  
[FogMode](FogMode.html)| Fog mode to use.  
[Folder](WSA.Folder.html)| List of accessible folders on Windows Store Apps.  
[ForcedCrashCategory](Diagnostics.ForcedCrashCategory.html)| Specifies the
category of crash to cause when calling ForceCrash().  
[FormatSwizzle](Rendering.FormatSwizzle.html)| Graphics Format Swizzle.  
[FoveatedRenderingCaps](Rendering.FoveatedRenderingCaps.html)| Capabilities of
the foveated rendering implementation.  
[FoveatedRenderingMode](Rendering.FoveatedRenderingMode.html)| Operation mode
for the foveated rendering system.  
[FrameCaptureDestination](Apple.FrameCaptureDestination.html)| Destination of
Frame Capture This is a wrapper for MTLCaptureDestination.  
[FullScreenMode](FullScreenMode.html)| Sets the full-screen mode. For
information on platform compatibility, refer to the description of each mode.  
[FullScreenMovieControlMode](FullScreenMovieControlMode.html)| Describes
options for displaying movie playback controls.  
[FullScreenMovieScalingMode](FullScreenMovieScalingMode.html)| Describes
scaling modes for displaying movies.  
[GizmoSubset](Rendering.GizmoSubset.html)| Specifies whether gizmos render
before or after postprocessing for a camera render.  
[GradientMode](GradientMode.html)| Color interpolation mode used by Gradient.  
[GraphicsDeviceType](Rendering.GraphicsDeviceType.html)| Graphics device API
type.  
[GraphicsFenceType](Rendering.GraphicsFenceType.html)| The type of
GraphicFence.  
[GraphicsFormat](Experimental.Rendering.GraphicsFormat.html)| Use this format
to create either Textures or RenderTextures from scripts.  
[GraphicsFormatUsage](Experimental.Rendering.GraphicsFormatUsage.html)| Use
this format usages to figure out the capabilities of specific GraphicsFormat  
[GraphicsTextureDescriptorFlags](Rendering.GraphicsTextureDescriptorFlags.html)|
The rendering and read/write access mode of a GraphicsTexture.  
[GraphicsTextureState](Rendering.GraphicsTextureState.html)| The state of a
GraphicsTexture.  
[GraphicsTier](Rendering.GraphicsTier.html)| An enum that represents graphics
tiers.  
[HDRDisplayBitDepth](HDRDisplayBitDepth.html)| Options for the number of bits
for HDR output in each color channel of swap chain buffers. Applicable when an
HDR display is active.  
[HDRDisplaySupportFlags](HDRDisplaySupportFlags.html)| A set of flags that
describe the level of HDR display support available on the GPU and driver.  
[HideFlags](HideFlags.html)| Bit mask that controls object destruction, saving
and visibility in inspectors.  
[IndexFormat](Rendering.IndexFormat.html)| Format of the mesh index buffer
data.  
[InspectorSort](InspectorSort.html)| Defines if enum should be shown sorted by
name or by value.  
[InspectorSortDirection](InspectorSortDirection.html)| Defines if enum should
be shown in ascending or descending order.  
[IntegrityCheckLevel](IntegrityCheckLevel.html)|  Enumeration specifying a
integrity check level.Additional resources: Debug.CheckIntegrity  
[KeyCode](KeyCode.html)| Key codes returned by Event.keyCode. These map
directly to a physical key on the keyboard. If "Use Physical Keys" is enabled
in Input Manager settings, these map directly to a physical key on the
keyboard. If "Use Physical Keys" is disabled these map to language dependent
mapping, different for every platform and cannot be guaranteed to work. "Use
Physical Keys" is enabled by default from 2022.1  
[LightEvent](Rendering.LightEvent.html)| Defines a place in light's rendering
to attach CommandBuffer objects to.  
[LightmapBakeType](LightmapBakeType.html)| Enum describing what part of a
light contribution can be baked.  
[LightmapCompression](LightmapCompression.html)| A set of options for the
level of compression the Editor uses for lightmaps.  
[LightmapsMode](LightmapsMode.html)| Lightmap (and lighting) configuration
mode, controls how lightmaps interact with lighting and what kind of
information they store.  
[LightmapsModeLegacy](LightmapsModeLegacy.html)| Single, dual, or directional
lightmaps rendering mode, used only in GIWorkflowMode.Legacy  
[LightMode](Experimental.GlobalIllumination.LightMode.html)| The lightmode. A
light can be real-time, mixed, baked or unknown. Unknown lights will be
ignored by the baking backends.  
[LightProbeOutsideHullStrategy](Rendering.LightProbeOutsideHullStrategy.html)|
Defines the way Unity chooses a probe to light a Renderer that is lit by Light
Probes but positioned outside the bounds of the Light Probe tetrahedral hull.  
[LightProbeUsage](Rendering.LightProbeUsage.html)| Light probe interpolation
type.  
[LightRenderMode](LightRenderMode.html)| How the Light is rendered.  
[LightShadowCasterMode](LightShadowCasterMode.html)| Allows mixed lights to
control shadow caster culling when Shadowmasks are present.  
[LightShadowResolution](Rendering.LightShadowResolution.html)| Shadow
resolution options for a Light.  
[LightShadows](LightShadows.html)| Shadow casting options for a Light.  
[LightType](LightType.html)| The type of a Light.  
[LightType](Experimental.GlobalIllumination.LightType.html)| The light type.  
[LightUnit](Rendering.LightUnit.html)| The unit of a Light's intensity.  
[LineAlignment](LineAlignment.html)| Control the direction lines face, when
using the LineRenderer or TrailRenderer.  
[LineTextureMode](LineTextureMode.html)| Choose how textures are applied to
Lines and Trails.  
[LoadSceneMode](SceneManagement.LoadSceneMode.html)| Used when loading a Scene
in a player.  
[LocalPhysicsMode](SceneManagement.LocalPhysicsMode.html)| Provides options
for 2D and 3D local physics.  
[LODFadeMode](LODFadeMode.html)| The LOD (level of detail) fade modes. Modes
other than LODFadeMode.None will result in Unity calculating a blend factor
for blending/interpolating between two neighbouring LODs and pass it to your
shader.  
[LogOption](LogOption.html)| Option flags for specifying special treatment of
a log message.  
[LogType](LogType.html)| The type of the log message in Debug.unityLogger.Log
or delegate registered with Application.RegisterLogCallback.  
[MarkerFlags](Unity.Profiling.LowLevel.MarkerFlags.html)| Profiler marker
usage flags.  
[MaterialGlobalIlluminationFlags](MaterialGlobalIlluminationFlags.html)| How
the material interacts with lightmaps and lightprobes.  
[MaterialPropertyType](MaterialPropertyType.html)| The type of a given
material property.  
[MeshTopology](MeshTopology.html)| Topology of Mesh faces.  
[MeshUpdateFlags](Rendering.MeshUpdateFlags.html)| Mesh data update flags.  
[MixedLightingMode](MixedLightingMode.html)| Enum describing what lighting
mode to be used with Mixed lights.  
[MotionVectorGenerationMode](MotionVectorGenerationMode.html)| The type of
motion vectors that should be generated.  
[NativeArrayOptions](Unity.Collections.NativeArrayOptions.html)| Options for
controlling how memory is cleared.  
[NativeLeakDetectionMode](Unity.Collections.NativeLeakDetectionMode.html)|
Sets which native leak memory leak detection mode to use.  
[NetworkReachability](NetworkReachability.html)| Describes network
reachability options.  
[NPOTSupport](NPOTSupport.html)| NPOT textures support.  
[OpaqueSortMode](Rendering.OpaqueSortMode.html)| Opaque object sorting mode of
a Camera.  
[OpenGLESVersion](Rendering.OpenGLESVersion.html)| Specifies the OpenGL ES
version.  
[OperatingSystemFamily](OperatingSystemFamily.html)| Enumeration for
SystemInfo.operatingSystemFamily.  
[PassType](Rendering.PassType.html)| Shader pass type for Unity's lighting
pipeline.  
[PerObjectData](Rendering.PerObjectData.html)| What kind of per-object data to
setup during rendering.  
[PersistentListenerMode](Events.PersistentListenerMode.html)| The mode that a
listener is operating in.  
[PhotoCaptureFileOutputFormat](Windows.WebCam.PhotoCaptureFileOutputFormat.html)|
Image Encoding Format.  
[PlayableTraversalMode](Playables.PlayableTraversalMode.html)| Traversal mode
for Playables.  
[PlayState](Playables.PlayState.html)| Status of a Playable.  
[PrimitiveType](PrimitiveType.html)| The various primitives that can be
created using the GameObject.CreatePrimitive function.  
[Priority](Unity.IO.LowLevel.Unsafe.Priority.html)| The priority level
attached to the AsyncReadManager read request.  
[ProcessingState](Unity.IO.LowLevel.Unsafe.ProcessingState.html)| The state of
the read request at the time of retrieval of AsyncReadManagerMetrics.  
[ProfilerArea](Profiling.ProfilerArea.html)| The different areas of profiling,
corresponding to the charts in ProfilerWindow.  
[ProfilerCategoryColor](Unity.Profiling.ProfilerCategoryColor.html)| Profiler
category colors enum.  
[ProfilerCategoryFlags](Unity.Profiling.ProfilerCategoryFlags.html)| Options
for determining if a Profiler category is built into Unity by default.  
[ProfilerFlowEventType](Unity.Profiling.ProfilerFlowEventType.html)| Defines
Profiler flow event type.  
[ProfilerMarkerDataType](Unity.Profiling.LowLevel.ProfilerMarkerDataType.html)|
Options for the Profiler metadata type.  
[ProfilerMarkerDataUnit](Unity.Profiling.ProfilerMarkerDataUnit.html)| Options
for Profiler marker data unit types.  
[ProfilerRecorderOptions](Unity.Profiling.ProfilerRecorderOptions.html)|
ProfilerRecorder lifecycle and collection options.  
[RayTracingAccelerationStructureBuildFlags](Rendering.RayTracingAccelerationStructureBuildFlags.html)|
Specifies how Unity builds the acceleration structure on the GPU.  
[RayTracingInstanceCullingFlags](Rendering.RayTracingInstanceCullingFlags.html)|
Flags used by RayTracingAccelerationStructure.CullInstances.  
[RayTracingMode](Experimental.Rendering.RayTracingMode.html)| Indicates how a
Renderer is updated.  
[RayTracingSubMeshFlags](Rendering.RayTracingSubMeshFlags.html)| Flags that
determine how rays intersect the geometry for each submesh relative to
Material type during ray tracing.  
[ReadStatus](Unity.IO.LowLevel.Unsafe.ReadStatus.html)| The state of an
asynchronous file request.  
[RealtimeGICPUUsage](Rendering.RealtimeGICPUUsage.html)| How much CPU usage to
assign to the final lighting calculations at runtime.  
[ReceiveGI](ReceiveGI.html)| This property only takes effect if you enable a
global illumination setting such as Baked Global Illumination or Enlighten
Realtime Global Illumination for the target Scene. When you enable ReceiveGI,
you can determine whether illumination data at runtime will come from Light
Probes or Lightmaps. When you set ReceiveGI to Lightmaps, the Mesh Renderer
receives global illumination from lightmaps. That means the Renderer is
included in lightmap atlases, possibly increasing their size, memory
consumption and storage costs. Calculating global illumination values for
texels in this Renderer also adds to bake times. When you set ReceiveGI to
Light Probes, the Mesh Renderer is not assigned space in lightmap atlases.
Instead it receives global illumination stored by Light Probes in the target
Scene. This can reduce bake times by avoiding the memory consumption and
storage cost associated with lightmaps. ReceiveGI is only editable if you
enable StaticEditorFlags.ContributeGI for the GameObject associated with the
target Mesh Renderer. Otherwise this property defaults to the Light Probes
setting.  
[ReflectionCubemapCompression](Rendering.ReflectionCubemapCompression.html)|
Determines how Unity will compress baked reflection cubemap.  
[ReflectionProbeClearFlags](Rendering.ReflectionProbeClearFlags.html)| Values
for ReflectionProbe.clearFlags, determining what to clear when rendering a
ReflectionProbe.  
[ReflectionProbeMode](Rendering.ReflectionProbeMode.html)| Reflection probe's
update mode.  
[ReflectionProbeRefreshMode](Rendering.ReflectionProbeRefreshMode.html)| An
enum describing the way a real-time reflection probe refreshes in the Player.  
[ReflectionProbeSortingCriteria](Rendering.ReflectionProbeSortingCriteria.html)|
Visible reflection probes sorting options.  
[ReflectionProbeTimeSlicingMode](Rendering.ReflectionProbeTimeSlicingMode.html)|
When a probe's ReflectionProbe.refreshMode is set to
ReflectionProbeRefreshMode.EveryFrame, this enum specify whether or not Unity
should update the probe's cubemap over several frames or update the whole
cubemap in one frame. Updating a probe's cubemap is a costly operation. Unity
needs to render the entire Scene for each face of the cubemap, as well as
perform special blurring in order to get glossy reflections. The impact on
frame rate can be significant. Time-slicing helps maintaning a more constant
frame rate during these updates by performing the rendering over several
frames.  
[ReflectionProbeUsage](Rendering.ReflectionProbeUsage.html)| Reflection Probe
usage.  
[RenderBufferLoadAction](Rendering.RenderBufferLoadAction.html)| This enum
describes what should be done on the render target when it is activated
(loaded).  
[RenderBufferStoreAction](Rendering.RenderBufferStoreAction.html)| This enum
describes what should be done on the render target when the GPU is done
rendering into it.  
[RendererListStatus](Rendering.RendererListStatus.html)| Options that
represent the result of a ScriptableRenderContext.QueryRendererList operation.  
[RenderingPath](RenderingPath.html)| Rendering path of a Camera.  
[RenderingThreadingMode](Rendering.RenderingThreadingMode.html)| Options for
the application's actual rendering threading mode.  
[RenderQueue](Rendering.RenderQueue.html)| Determine in which order objects
are renderered.  
[RenderStateMask](Rendering.RenderStateMask.html)| Specifies which parts of
the render state that is overriden.  
[RenderTargetFlags](Rendering.RenderTargetFlags.html)| This enum describes
optional flags for the RenderTargetBinding structure.  
[RenderTextureCreationFlags](RenderTextureCreationFlags.html)| Set of flags
that control the state of a newly-created RenderTexture.  
[RenderTextureFormat](RenderTextureFormat.html)| Format of a RenderTexture.  
[RenderTextureMemoryless](RenderTextureMemoryless.html)| Flags enumeration of
the render texture memoryless modes.  
[RenderTextureReadWrite](RenderTextureReadWrite.html)| Color space conversion
mode of a RenderTexture.  
[RenderTextureSubElement](Rendering.RenderTextureSubElement.html)| Types of
data that you can encapsulate within a render texture.  
[RTClearFlags](Rendering.RTClearFlags.html)| Flags that determine which render
targets Unity clears when you use CommandBuffer.ClearRenderTarget.  
[RuntimeInitializeLoadType](RuntimeInitializeLoadType.html)| Specifies when to
get a callback during the startup of the runtime or when entering play mode in
the Editor. Used with RuntimeInitializeOnLoadMethodAttribute.  
[RuntimePlatform](RuntimePlatform.html)| The platform application is running.
Returned by Application.platform.  
[ScheduleMode](Unity.Jobs.LowLevel.Unsafe.ScheduleMode.html)| Options for
scheduling a managed job.  
[ScreenOrientation](ScreenOrientation.html)| Describes screen orientation.  
[SearchType](Rendering.SearchType.html)| Describe how to use the path in
ResourcePathsBaseAttribute.  
[SearchViewFlags](Search.SearchViewFlags.html)| Search view flags used to open
the Object Picker in various states.  
[SendMessageOptions](SendMessageOptions.html)| Options for how to send a
message.  
[ShaderConstantType](Rendering.ShaderConstantType.html)| Options for the
shader constant value type.  
[ShaderKeywordType](Rendering.ShaderKeywordType.html)| Type of a shader
keyword, eg: built-in or user defined.  
[ShaderParamType](Rendering.ShaderParamType.html)| Options for the data type
of a shader constant's members.  
[ShaderPropertyFlags](Rendering.ShaderPropertyFlags.html)| Flags that control
how a shader property behaves.  
[ShaderPropertyType](Rendering.ShaderPropertyType.html)| Type of a given
shader property.  
[ShadowCastingMode](Rendering.ShadowCastingMode.html)| How shadows are cast
from this object.  
[ShadowMapPass](Rendering.ShadowMapPass.html)| Allows precise control over
which shadow map passes to execute CommandBuffer objects attached using
Light.AddCommandBuffer.  
[ShadowmaskMode](ShadowmaskMode.html)| The rendering mode of Shadowmask.  
[ShadowObjectsFilter](ShadowObjectsFilter.html)| The filters that Unity can
use when it renders GameObjects in the shadow pass.  
[ShadowProjection](ShadowProjection.html)| Shadow projection type for Quality
Settings.  
[ShadowQuality](ShadowQuality.html)| Determines which type of shadows should
be used.  
[ShadowResolution](ShadowResolution.html)| Default shadow resolution. Each
decrease in quality level halves the resolution of shadows.  
[ShadowSamplingMode](Rendering.ShadowSamplingMode.html)| Used by
CommandBuffer.SetShadowSamplingMode.  
[SinglePassStereoMode](Rendering.SinglePassStereoMode.html)| Enum type defines
the different stereo rendering modes available.  
[SkinQuality](SkinQuality.html)| The maximum number of bones affecting a
single vertex.  
[SkinWeights](SkinWeights.html)| Skin weights.  
[SnapAxis](SnapAxis.html)| Defines the axes that can be snapped.  
[SortingCriteria](Rendering.SortingCriteria.html)| How to sort objects during
rendering.  
[Space](Space.html)| The coordinate spaces in which to apply transformation to
a GameObject.  
[SpeechError](Windows.Speech.SpeechError.html)| Represents an error in a
speech recognition system.  
[SpeechSystemStatus](Windows.Speech.SpeechSystemStatus.html)| Represents the
current status of the speech recognition system or a dictation recognizer.  
[SpriteAlignment](SpriteAlignment.html)| How a Sprite's graphic rectangle is
aligned with its pivot point.  
[SpriteDrawMode](SpriteDrawMode.html)|  SpriteRenderer draw mode.  
[SpriteMaskInteraction](SpriteMaskInteraction.html)| This enum controls the
mode under which the sprite will interact with the masking system.  
[SpriteMeshType](SpriteMeshType.html)| Defines the type of mesh generated for
a sprite.  
[SpritePackingMode](SpritePackingMode.html)| Sprite packing modes for the
Sprite Packer.  
[SpritePackingRotation](SpritePackingRotation.html)| Sprite rotation modes for
the Sprite Packer.  
[SpriteSortPoint](SpriteSortPoint.html)| Determines the position of the Sprite
used for sorting the Renderer.  
[SpriteTileMode](SpriteTileMode.html)| Tiling mode for
SpriteRenderer.tileMode.  
[StackTraceLogType](StackTraceLogType.html)| Stack trace logging options.  
[StencilOp](Rendering.StencilOp.html)| Specifies the operation that's
performed on the stencil buffer when rendering.  
[StereoTargetEyeMask](StereoTargetEyeMask.html)| Enum values for the Camera's
targetEye property.  
[SubPassFlags](Rendering.SubPassFlags.html)| Flags to indicate specialized
native subpass behaviour.  
[SynchronisationStage](Rendering.SynchronisationStage.html)| The stages of the
draw call processing on the GPU.  
[SynchronisationStageFlags](Rendering.SynchronisationStageFlags.html)|
Describes the various stages of GPU processing against which the GraphicsFence
can be set and waited against.  
[SystemGestureDeferMode](iOS.SystemGestureDeferMode.html)| Bit-mask used to
control the deferring of system gestures on iOS.  
[SystemLanguage](SystemLanguage.html)| The language the user's operating
system is running in. Returned by Application.systemLanguage.  
[TerrainQualityOverrides](TerrainQualityOverrides.html)| Flags used by
QualitySettings to specify which Terrain fields the quality settings should
override.  
[TextureDimension](Rendering.TextureDimension.html)| Texture "dimension"
(type).  
[TextureFormat](TextureFormat.html)| Format used when creating textures from
scripts.  
[TextureMipmapLimitBiasMode](TextureMipmapLimitBiasMode.html)| An enumeration
that represents the bias mode to use for TextureMipmapLimitSettings.limitBias.  
[TextureWrapMode](TextureWrapMode.html)| Wrap mode for textures.  
[ThreadPriority](ThreadPriority.html)| Priority of a thread.  
[TileForegroundText](WSA.TileForegroundText.html)| Style for foreground text
on a secondary tile.  
[TileTemplate](WSA.TileTemplate.html)| Templates for various tile styles.  
[ToastTemplate](WSA.ToastTemplate.html)| Templates for various toast styles.  
[TouchScreenKeyboardType](TouchScreenKeyboardType.html)| Enumeration of the
different types of supported touchscreen keyboards.  
[TransferFunction](TransferFunction.html)| Contains electro-optical transfer
function options.  
[TransparencySortMode](TransparencySortMode.html)| Transparent object sorting
mode of a Camera.  
[UISubset](Rendering.UISubset.html)| Bit mask that specifies which UI subset
to render when calling ScriptableRenderContext.CreateUIOverlayRendererList.
For any frame, UI subsets must be rendered in the following order:
UIToolkit_UGUI, LowLevel.  
[UnityEventCallState](Events.UnityEventCallState.html)| Controls the scope of
UnityEvent callbacks.  
[UnloadSceneOptions](SceneManagement.UnloadSceneOptions.html)| Scene unloading
options passed to SceneManager.UnloadScene.  
[UserAuthorization](UserAuthorization.html)| Constants to pass to
Application.RequestUserAuthorization.  
[ValidationLevel](ValidationLevel.html)|  Enumeration specifying a validation
level.Additional resources: Debug.IsValidationLevelEnabled  
[VertexAttribute](Rendering.VertexAttribute.html)| Possible attribute types
that describe a vertex in a Mesh.  
[VertexAttributeFormat](Rendering.VertexAttributeFormat.html)| Data type of a
VertexAttribute.  
[VideoShadersIncludeMode](Rendering.VideoShadersIncludeMode.html)| Video
shaders mode used by GraphicsSettings.  
[VRTextureUsage](VRTextureUsage.html)| This enum describes how the
RenderTexture is used as a VR eye texture. Instead of using the values of this
enum manually, use the value returned by eyeTextureDesc or other VR functions
returning a RenderTextureDescriptor.  
[WaitTimeoutMode](WaitTimeoutMode.html)|  Determines which mode of time
measurement to use in wait operations.  
[WebCamMode](Windows.WebCam.WebCamMode.html)| Describes the active mode of the
Web Camera resource.  
[WeightedMode](WeightedMode.html)| Sets which weights to use when calculating
curve segments.  
[WhitePoint](WhitePoint.html)| The reference white point of a color space.  
[WindowActivationState](WSA.WindowActivationState.html)| Specifies the set of
reasons that a windowActivated event was raised.  
[WrapMode](WrapMode.html)| Determines how time is treated outside of the
keyframed range of an AnimationClip or AnimationCurve.  
  
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

