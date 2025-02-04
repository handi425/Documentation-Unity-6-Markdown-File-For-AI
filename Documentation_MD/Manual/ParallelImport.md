[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/ParallelImport.html)
  * [中文](/cn/current/Manual/ParallelImport.html)
  * [日本語](/ja/current/Manual/ParallelImport.html)
  * [한국어](/kr/current/Manual/ParallelImport.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/ParallelImport.html)
  * [中文](/cn/current/Manual/ParallelImport.html)
  * [日本語](/ja/current/Manual/ParallelImport.html)
  * [한국어](/kr/current/Manual/ParallelImport.html)

  * [Working in Unity](working-in-unity.html)
  * [Assets and media](assets-and-media.html)
  * [Asset workflow](AssetWorkflow.html)
  * [Importing assets](ImportingAssets.html)
  * Importing assets simultaneously

[](ImportingAssets.html)

Importing assets

[](AssetTypes.html)

Supported Asset Types

## Importing assets simultaneously

By default, Unity imports assets one after another sequentially on the main
Editor process. However, Unity also supports parallel importing for some types
of asset. Parallel importing uses multiple processes to import assets
simultaneously, which is faster than the default sequential method of
importing.

To enable parallel importing, go to **Edit** > **Project Settings** >
**Editor** , then under the **Asset Pipeline** section, enable the **Parallel
Import** checkbox.

![The Parallel Import option in the Project Settings
window.](../uploads/Main/ParallelImportEnable.png) The Parallel Import option
in the Project Settings window.

## The scope of parallel imports

Unity’s **Parallel Import** feature supports only certain types of asset. It
applies only when the Editor is performing its standard asset database
refresh, which occurs when it detects new or modified assets in the Project
folder and automatically imports them.

The specific types of asset which Unity can import in parallel are:

  * Image file types imported by the [Texture Importer](ImportingTextures.html)
  * **Model file** A file containing a 3D data, which may include definitions for meshes, bones, animation, materials and textures. [More info](3D-formats.html)  
See in [Glossary](Glossary.html#Modelfile) types imported by the [Model
Importer](ImportingModelFiles.html)

Other types of asset are always imported sequentially during an asset database
refresh.

Some Asset Database API methods also respect this setting, if you use them to
import, refresh, or create Texture or Model assets. These are:

  * [AssetDatabase.ImportAsset](../ScriptReference/AssetDatabase.ImportAsset.html)
  * [AssetDatabase.Refresh](../ScriptReference/AssetDatabase.Refresh.html)
  * [AssetDatabase.CreateAsset](../ScriptReference/AssetDatabase.CreateAsset.html)

## Implications for AssetPostprocessors

Because parallel imports operate in a separate worker instance of the Unity
editor any [AssetPostprocessors](../ScriptReference/AssetPostprocessor.html)
handling Texture or Model imports will also take effect in that instance
rather than the main Editor process.

Any side effects of these processors can cause unexpected problems. For
example, if you modify a static variable on a C# class during the execution of
a post process, that modification will not affect the code running in the
Editor.

Any code that you write for post processors should always be self-contained,
deterministic, and shouldn’t change the context it’s running in. For example,
it shouldn’t change the Editor settings or create new assets on disk.

Following these rules helps your processor code avoid parallel threading
issues and ensures that the results are always consistent.

## Controlling the import worker processes

In the Asset Pipeline settings, there are three settings that allow you to
control the behaviour of the import worker processes. These settings are
project-specific.

![The import worker process controls, in the Project Settings
window.](../uploads/Main/ParallelImportWorkers.png) The import worker process
controls, in the Project Settings window.

**Property name** | **Description**  
---|---  
**Desired Import Worker Count** | The number of import worker processes that the import pipeline considers the optimal number to run in parallel.  
**Standby Import Worker Count** | The minimum number of worker processes to keep, even if they’re idle.  
  
If there are more worker processes than this, Unity shuts down import workers
that have been idle for some time, to free up system resources. This property
allows you to manage how Unity balances system resources when some processes
are idle, compared with the time it takes to start up new import worker
processes.  
  
You might see an improvement in import performance by increasing this value if
you are frequently iterating on model, animation or texture work, and are
therefore frequently importing batches of models or image files.  
**Idle Import Worker Shutdown Delay** | The amount of time in seconds to wait before shutting down an idle worker.  
  
You can also control the default values that Unity sets the **Desired Import
Worker Count** for new projects. To do this, go to **Preferences** > **Asset
Pipeline** > **Import Worker Count %**.

![The Importer Worker Count setting in the Preferences
window.](../uploads/Main/ParallelImportWorkers2.png) The Importer Worker Count
setting in the Preferences window.

When you create a new project, Unity uses the **Import Worker Count %** value
to assign your project’s **Desired Import Worker Count** value to the
percentage of the number of logical cores available on your system.

For example, if your system has 16 logical cores and this preference is set to
25%, the **Desired Import Worker Count** for new projects is 4. If you set
this value too high, your import worker processes need to compete over other
processes and system resources such as reading and writing files. The default
value of 25% is suitable for most situations.

[](ImportingAssets.html)

Importing assets

[](AssetTypes.html)

Supported Asset Types

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

