[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/AsyncReadManagerMetrics.html)
  * [中文](/cn/current/Manual/AsyncReadManagerMetrics.html)
  * [日本語](/ja/current/Manual/AsyncReadManagerMetrics.html)
  * [한국어](/kr/current/Manual/AsyncReadManagerMetrics.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/AsyncReadManagerMetrics.html)
  * [中文](/cn/current/Manual/AsyncReadManagerMetrics.html)
  * [日本語](/ja/current/Manual/AsyncReadManagerMetrics.html)
  * [한국어](/kr/current/Manual/AsyncReadManagerMetrics.html)

  * [Working in Unity](working-in-unity.html)
  * [Assets and media](assets-and-media.html)
  * [Asset workflow](AssetWorkflow.html)
  * [Optimizing assets](assets-optimizing.html)
  * Asset loading metrics

[](profiler-asset-loading-module.html)

Asset Loading Profiler module

[](AssetStore.html)

Unity's Asset Store

# Asset loading metrics

Use the
[AsyncReadManagerMetrics](../ScriptReference/Unity.IO.LowLevel.Unsafe.AsyncReadManagerMetrics.html)
class to monitor runtime asset loading and file reading performance. This
class records data about all the file read operations managed by the
[AsyncReadManager](../ScriptReference/Unity.IO.LowLevel.Unsafe.AsyncReadManager.html).

The Unity Engine uses the
[AsyncReadManager](../ScriptReference/Unity.IO.LowLevel.Unsafe.AsyncReadManager.html)
to read most files at runtime. The files loaded with the AsyncReadManager
include AssetBundles, Addressables and Resources. In addition, you can load
files from **scripts** A piece of code that allows you to create your own
Components, trigger game events, modify Component properties over time and
respond to user input in any way you like. [More info](creating-scripts.html)  
See in [Glossary](Glossary.html#Scripts) using
[AsyncReadManager.Read](../ScriptReference/Unity.IO.LowLevel.Unsafe.AsyncReadManager.Read.html).

The
[AsyncReadManagerMetrics](../ScriptReference/Unity.IO.LowLevel.Unsafe.AsyncReadManagerMetrics.html)
class allows you to enable metrics collection and retrieve the recorded
metrics data. You can also filter and summarize the recorded data to help your
analysis. This metrics information can help you identify problem areas
involving asset loading as well as measure the impact that your changes have
on asset loading performance.

The
[AsyncReadManagerMetrics](../ScriptReference/Unity.IO.LowLevel.Unsafe.AsyncReadManagerMetrics.html)
class is _only_ available in **development builds** A development build
includes debug symbols and enables the Profiler. [More
info](https://docs.unity.com/devops/en/manual/build-target-
configurations#Build_target_advanced_settings_overview)  
See in [Glossary](Glossary.html#DevelopmentBuild). You must guard any calls to
the AsyncReadManagerMetrics APIs inside an #if preprocessor directive using
the `ENABLE_PROFILER` symbol. The `ENABLE_PROFILER` symbol is only defined for
development builds, so this allows your scripts to compile in builds where the
metrics are unavailable. For backwards compatibility, you can also use the
`UNITY_2020_2_OR_NEWER` symbol to remove the metrics code from earlier
versions of Unity. For example:

    
    
    #if ENABLE_PROFILER && UNITY_2020_2_OR_NEWER
        AsyncReadManagerMetrics.StartCollectingMetrics();
    #endif
    

## Enabling metric collection

You must enable metrics collection before any data is recorded. Enable metrics
collection with one of the following methods:

  * Calling [AsyncReadManagerMetrics.StartCollectingMetrics](../ScriptReference/Unity.IO.LowLevel.Unsafe.AsyncReadManagerMetrics.StartCollectingMetrics.html)
  * Passing **-enable-file-read-metrics** as a command line argument when launching your application

**Note:** you can pass **-enable-file-read-metrics** when launching the Unity
Editor application to enable collection on entering Play mode. However, the
Editor loads some categories of assets, such as textures, itself and does not
reload them when you enter Playmode. To get a full picture of your file IO
metrics, you must collect data from a development build of your application.

## Getting metric data

Retrieve the metrics collected by the
[AsyncReadManagerMetrics](../ScriptReference/Unity.IO.LowLevel.Unsafe.AsyncReadManagerMetrics.html)
class by calling
[GetMetrics](../ScriptReference/Unity.IO.LowLevel.Unsafe.AsyncReadManagerMetrics.GetMetrics.html).
Pass an
[AsyncReadManagerMetrics.Flags](../ScriptReference/Unity.IO.LowLevel.Unsafe.AsyncReadManagerMetrics.Flags.html)
to this function to specify whether or not to clear the metrics after
retrieval. Clear the metrics to remove all the completed (including cancelled
and failed) reads from the stored metrics. Clearing doesn’t affect any queued
or in-process operations; you can access the metrics for unfinished operations
by calling
[GetMetrics](../ScriptReference/Unity.IO.LowLevel.Unsafe.AsyncReadManagerMetrics.GetMetrics.html)
again after they complete. By clearing the metrics regularly, you can avoid
rereading the same data and also reduce the data overhead of the system.

    
    
    #if ENABLE_PROFILER && UNITY_2020_2_OR_NEWER
        AsyncReadManagerRequestMetric[] metrics 
            = AsyncReadManagerMetrics.GetMetrics(AsyncReadManagerMetrics.Flags.ClearOnRead);
    #endif
    
    

Where possible, the metric data includes context information about a read
operation. This information includes the
[AssetLoadingSubsystem](../ScriptReference/Unity.IO.LowLevel.Unsafe.AssetLoadingSubsystem.html)
that requested the read, the
[AssetName](../ScriptReference/Unity.IO.LowLevel.Unsafe.AsyncReadManagerRequestMetric.AssetName.html),
and the
[AssetTypeID](../ScriptReference/Unity.IO.LowLevel.Unsafe.AsyncReadManagerRequestMetric.AssetTypeId.html).
When the AsyncReadManager doesn’t have access to this information, the value
for these metrics fields is
[Other](../ScriptReference/Unity.IO.LowLevel.Unsafe.AssetLoadingSubsystem.Other.html),
empty, and zero, respectively.

**Note:** The Asset TypeIDs currently known to be supported are shown in the
table below. For other TypeIDs that may appear, please see [YAML Class ID
Reference](ClassIDReference.html).

TypeID | Type Name  
---|---  
28 | Texture2D  
117 | Texture3D  
89 | **CubeMap** A collection of six square textures that can represent the reflections in an environment or the skybox drawn behind your geometry. The six squares form the faces of an imaginary cube that surrounds an object; each face represents the view along the directions of the world axes (up, down, left, right, forward and back). [More info](class-Cubemap-landing.html)  
See in [Glossary](Glossary.html#Cubemap)  
43 | Mesh  
  
## Getting summarized data

You can get a summary of the AsyncReadManager metrics with the following
methods:

  * [GetCurrentSummaryMetrics](../ScriptReference/Unity.IO.LowLevel.Unsafe.AsyncReadManagerMetrics.GetCurrentSummaryMetrics.html) – returns a summary of all the metrics collected since the last time you cleared the metric store.
  * [GetSummaryOfMetrics](../ScriptReference/Unity.IO.LowLevel.Unsafe.AsyncReadManagerMetrics.GetSummaryOfMetrics.html) – returns a summary of the metrics in an array of [AsyncReadManagerRequestMetric](../ScriptReference/Unity.IO.LowLevel.Unsafe.AsyncReadManagerRequestMetric.html), which you can get by calling [GetMetrics](../ScriptReference/Unity.IO.LowLevel.Unsafe.AsyncReadManagerMetrics.GetMetrics.html).

For example:

    
    
    #if ENABLE_PROFILER && UNITY_2020_2_OR_NEWER
        AsyncReadManagerSummaryMetrics summaryOfMetrics 
            = AsyncReadManagerMetrics.GetCurrentSummaryMetrics(AsyncReadManagerMetrics.Flags.ClearOnRead);
    #endif
    

Or:

    
    
    #if ENABLE_PROFILER && UNITY_2020_2_OR_NEWER
        AsyncReadManagerRequestMetric[] metrics 
            = AsyncReadManagerMetrics.GetMetrics(AsyncReadManagerMetrics.Flags.ClearOnRead);
        AsyncReadManagerSummaryMetrics summaryOfMetrics 
            = AsyncReadManagerMetrics.GetSummaryOfMetrics(metrics);
    #endif
    

Summary data for the metrics includes statistics such as:

  * Average bandwidth
  * Average read size
  * Asset type with longest load time
  * Number of reads
  * Number of requests
  * Total bytes read

(See
[AsyncReadManagerSummaryMetrics](../ScriptReference/Unity.IO.LowLevel.Unsafe.AsyncReadManagerSummaryMetrics.html)
for a complete list.)

By default, the summarized statistics include all read operations, including
those that are queued or in-progress. You can use a filter to limit the
summary to those operations you are specifically interested in. For example,
you could use a filter to limit the summarized statistics to completed read
operations for texture assets.

**Note:** Calculating the summary statistics does require processing
resources. To prevent these calculations from changing the measurements you
are recording, you can collect the metrics first and only get the summary
after the operations you are analyzing have finished.

### Summary filters

Use
[AsyncReadManagerMetricsFilters](../ScriptReference/Unity.IO.LowLevel.Unsafe.AsyncReadManagerMetricsFilters.html)
with either of these methods to specify what types of data to summarize. Any
metrics that do not match a filter are excluded from the summary. You can
filter with the following categories:

  * Asset type (by [YAML ID](ClassIDReference.html))
  * [Processing state](../ScriptReference/Unity.IO.LowLevel.Unsafe.ProcessingState.html) (whether the read operation is queued, reading, completed, and so on)
  * [Read type](../ScriptReference/Unity.IO.LowLevel.Unsafe.FileReadType.html) (async or sync)
  * [Priority](../ScriptReference/Unity.IO.LowLevel.Unsafe.Priority.html) (high or low)
  * Subsystem ([AssetLoadingSubsystem](../ScriptReference/Unity.IO.LowLevel.Unsafe.AssetLoadingSubsystem.html))

You can set multiple categories for the same filter. A read operation must
match all categories for the metrics of that operation to be included in the
summary. For example, you can specify values for both the
[ProcessingState](../ScriptReference/Unity.IO.LowLevel.Unsafe.ProcessingState.html)
and the
[Subsystem](../ScriptReference/Unity.IO.LowLevel.Unsafe.AssetLoadingSubsystem.html)
of a filter to summarize only operations in the designated processing states
initiated by the designated subsytems.

You can also specify multiple values for a category. In this case, a read
operation can match any value you specify for a category for its metrics to be
included in the summary. For example, you can specify both
[Mesh](../ScriptReference/Unity.IO.LowLevel.Unsafe.AssetLoadingSubsystem.Mesh.html)The
main graphics primitive of Unity. Meshes make up a large part of your 3D
worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs,
Nurms, Subdiv surfaces must be converted to polygons. [More info](mesh.html)  
See in [Glossary](Glossary.html#Mesh) and
[Texture](../ScriptReference/Unity.IO.LowLevel.Unsafe.AssetLoadingSubsystem.Texture.html)An
image used when rendering a GameObject, Sprite, or UI element. Textures are
often applied to the surface of a mesh to give it visual detail. [More
info](class-TextureImporter.html)  
See in [Glossary](Glossary.html#texture) for the
[Subsystem](../ScriptReference/Unity.IO.LowLevel.Unsafe.AssetLoadingSubsystem.html)
category to summarize operations for both Mesh and Texture assets.

[](profiler-asset-loading-module.html)

Asset Loading Profiler module

[](AssetStore.html)

Unity's Asset Store

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

