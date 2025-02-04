[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/xrsdk-runtime-discovery.html)
  * [中文](/cn/current/Manual/xrsdk-runtime-discovery.html)
  * [日本語](/ja/current/Manual/xrsdk-runtime-discovery.html)
  * [한국어](/kr/current/Manual/xrsdk-runtime-discovery.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/xrsdk-runtime-discovery.html)
  * [中文](/cn/current/Manual/xrsdk-runtime-discovery.html)
  * [日本語](/ja/current/Manual/xrsdk-runtime-discovery.html)
  * [한국어](/kr/current/Manual/xrsdk-runtime-discovery.html)

  * [Platform development ](PlatformSpecific.html)
  * [XR](XR.html)
  * [Unity XR SDK](xr-sdk.html)
  * Runtime discovery and activation of subsystems

[](xrsdk-unity-subsystems-manifest-json.html)

UnitySubsystemsManifest.json

[](xrsdk-subsystems-landing.html)

Subsystems

# Runtime discovery and activation of subsystems

Add the following script to your project in order to scan for and create or
start a Display subsystem with the `id` of `Display0`. You can change the
`match` variable if you want to load other Display subsystems:

    
    
    using System;
    using System.Collections;
    using System.Collections.Generic;
    using UnityEngine;
    using UnityEngine.Experimental.XR;
    using UnityEngine.XR;
    
    public class Display : MonoBehaviour
    {
        public string match = "Display0";
    
        // Use this for initialization
        void Start ()
        {
            List<XRDisplaySubsystemDescriptor> displays = new List<XRDisplaySubsystemDescriptor>();
            SubsystemManager.GetSubsystemDescriptors(displays);
            Debug.Log("Number of display providers found: " + displays.Count);
    
            foreach (var d in displays)
            {
                Debug.Log("Scanning display id: " + d.id);
    
                if (d.id.Contains(match))
                {
                    Debug.Log("Creating display " + d.id);
                    XRDisplaySubsystem dispInst = d.Create();
    
                    if (dispInst != null)
                    {
                        Debug.Log("Starting display " + d.id);
                        dispInst.Start();
                    }
                }
            }
        }
    }
    

The [XR
Management](https://docs.unity3d.com/Packages/com.unity.xr.management@4.3/)
package is the user-facing **UI**(User Interface) Allows a user to interact
with your application. Unity currently supports three UI systems. [More
info](UI-system-compare.html)  
See in [Glossary](Glossary.html#UI) used to configure loading of subsystems at
runtime. It uses the same underlying APIs (described above) to create and
manage subsystems. If you want your provider to show up in the **XR** An
umbrella term encompassing Virtual Reality (VR), Augmented Reality (AR) and
Mixed Reality (MR) applications. Devices supporting these forms of interactive
applications can be referred to as XR devices. [More info](XR.html)  
See in [Glossary](Glossary.html#XR) Settings UI, write an
[XRLoader](https://docs.unity3d.com/Packages/com.unity.xr.management@4.3/manual/Provider.html).

If your **plug-in** A set of code created outside of Unity that creates
functionality in Unity. There are two kinds of plug-ins you can use in Unity:
Managed plug-ins (managed .NET assemblies created with tools like Visual
Studio) and Native plug-ins (platform-specific native code libraries). [More
info](./plug-ins.html)  
See in [Glossary](Glossary.html#Plug-in) fails to load, see the
troubleshooting section below.

## Troubleshooting plug-in discovery at runtime

To troubleshoot the initialization or starting of your subsystem Provider,
check the [editor log or player output log](log-files.html) for lines that
start with `[XR]` or `[Subsystems]`.

## No subsystems found in C#

If you just added a .json and plug-in files, make sure you relaunch Unity.
Currently, Unity only discovers these files at start-up. Also, make sure that
the Provider uses the correct [file layout](xrsdk-provider-setup.html#file-
layout).

## Errors finding and parsing the UnitySubsystemsManifest.json file

**Error** | **Description**  
---|---  
[XR] 3 ‘displays’ descriptors matched in Assets/UnityXRDisplayExample/UnitySubsystemsManifest.json | Unity successfully found display descriptors and registers three different `id`s for this plug-in.  
[XR] No descriptors matched for inputs in Assets/UnityXRDisplayExample/UnitySubsystemsManifest.json. | The .json file contains no input descriptors. This is normal if you’re not implementing an input subsystem.  
If you were expecting Unity to find descriptors in your .json file, they could
be malformed. See documentation on [UnitySubsystemsManifest.json](xrsdk-unity-
subsystems-manifest-json.html) for the correct format to use.  
[XR] Failed to parse json header for Assets/UnityXRDisplayExample/UnitySubsystemsManifest.json (did you forget to include name or libraryName fields?) | This likely means you have a malformed .json file. Run it through a validation tool, such as [json linter](https://jsonlint.com/).  
  
## Errors finding and loading the provider plug-in

**Error** | **Description**  
---|---  
[XR] PluginName failed to register Provider for DisplayId (json name or id doesn’t match?) | This means that the first two arguments to `RegisterLifecycleProvider` don’t match the .json file.  
The first argument, `pluginName`, should match the `name` field in the .json
file.  
The second argument, `id`, should match the `id` field of the subsystem in the
.json file.  
[XR] Unable to load plugin PluginName for subsystem DisplayId | Your plug-in couldn’t be found, it was built for the wrong architecture, or it has missing dependencies that need to be loaded. In the later case, you can use the [Dependency Walker](http://www.dependencywalker.com/) tool to find out if there are missing dependencies.  
  
## Errors initializing the provider

**Error** | **Description**  
---|---  
[XR] Failed to initialize subsystem DisplayId [error: 1] | Unity called out to your `Initialize` method, but it returned `kUnitySubsystemErrorCodeFailure`. Double-check the implementation of your `Initialize` method.  
  
[](xrsdk-unity-subsystems-manifest-json.html)

UnitySubsystemsManifest.json

[](xrsdk-subsystems-landing.html)

Subsystems

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

