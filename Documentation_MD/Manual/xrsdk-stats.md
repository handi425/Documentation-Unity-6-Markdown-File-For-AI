[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/xrsdk-stats.html)
  * [中文](/cn/current/Manual/xrsdk-stats.html)
  * [日本語](/ja/current/Manual/xrsdk-stats.html)
  * [한국어](/kr/current/Manual/xrsdk-stats.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/xrsdk-stats.html)
  * [中文](/cn/current/Manual/xrsdk-stats.html)
  * [日本語](/ja/current/Manual/xrsdk-stats.html)
  * [한국어](/kr/current/Manual/xrsdk-stats.html)

  * [Platform development ](PlatformSpecific.html)
  * [XR](XR.html)
  * [Unity XR SDK](xr-sdk.html)
  * Interfaces
  * XR SDK Stats interface

[](xrsdk-pre-init-interface.html)

XR SDK PreInit interface

[](UnityServices.html)

Unity Services

# XR SDK Stats interface

The **XR** An umbrella term encompassing Virtual Reality (VR), Augmented
Reality (AR) and Mixed Reality (MR) applications. Devices supporting these
forms of interactive applications can be referred to as XR devices. [More
info](XR.html)  
See in [Glossary](Glossary.html#XR) SDK Stats interface is used for
registering and managing statistics data.

## Overview

Use the XR Stats interface to record stats among the various subsystems. The
only supported stat primitive is a floating point number.

Use the `UnityPluginLoad` entry point method to acquire a pointer to the
XRStats interface:

    
    
    IUnityXRStats* sXRStats = nullptr;
    
    extern "C" void UNITY_INTERFACE_EXPORT UnityPluginLoad(IUnityInterfaces* unityInterfaces)
    {
        sXRStats = (IUnityXRStats*)unityInterfaces->GetInterface(UNITY_GET_INTERFACE_GUID(IUnityXRStats));
        //...
    }
    

## Usage

Register your subsystem and individual stat definitions with the stats
interface:

    
    
    static UnityXRStatId m_GPUFrameTimeID;
    static UnityXRStatId m_DroppedFrameCountID;
    static UnityXRStatId m_WorkThreadStat;
    
    static UnitySubsystemErrorCode ExampleDisplayProvider_Start(UnitySubsystemHandle handle)
    {
        if (sXRStats)
        {
            sXRStats->RegisterStatSource(handle);
            m_GPUFrameTimeID = sXRStats->RegisterStatDefinition(handle, "Example.GPUTime", kUnityXRStatOptionNone);
            m_DroppedFrameCountID = sXRStats->RegisterStatDefinition(handle, "Example.DroppedFrame", kUnityXRStatOptionNone);
            m_WorkThreadStat = sXRStats->RegisterStatDefinition(handle, "Example.WorkerThreadStat", kUnityXRStatOptionNone);
        }
    
        return kUnitySubsystemErrorCodeSuccess;
    }
    

Update stats on the Gfx Thread:

    
    
    extern float GetLastGPUTime(); //provided by your runtime
    static void ExampleDisplayProvider_GfxThreadCall(UnitySubsystemHandle handle)
    {
        sXRStats->SetStatFloat(m_GPUFrameTimeID, GetLastGPUTime());
        // Do gfx thread things
    }
    
    

Update stats on the main thread:

    
    
    extern float GetDroppedFrameCount(); //provided by your runtime
    
    static void ExampleDisplayProvider_MainThreadCall(UnitySubsystemHandle handle)
    {
        sXRStats->SetStatFloat(m_DroppedFrameCountID, GetDroppedFrameCount());
        // Do main thread things
    }
    

Update stats on your own threads, but be sure to call `IncrementStatFrame` to
keep the current frame for that thread in sync with the other threads (this is
managed internally for the main and graphics threads):

    
    
    extern float GetWorkerThreadStat(); //provided by your runtime
    static void ExampleDisplayProvider_MyWorkerThread(UnitySubsystemHandle handle)
    {
        sXRStats->IncrementStatFrame();
        sXRStats->SetStatFloat(m_WorkThreadStat, GetWorkerThreadStat());
        // Do worker thread things
    }
    

Unregister the stat source when the subsystem stops:

    
    
    static void ExampleDisplayProvider_Stop(UnitySubsystemHandle handle)
    {
        sXRStats->UnregisterStatSource(handle);
    }
    
    

## Thread safety

Updating stats via `SetStatFloat` is thread safe. However, registering and
unregistering stat sources is not thread safe and should only be done on the
main thread during the Start and Stop functions of the stat source’s
lifecycle.

## Limitations

The queue size for processing stats is 2000. This queue is shared amongst all
threads and all subsystems and is only serviced upon frame completion. For
this reason, you should keep the number of calls to `SetStatFloat` low to
avoid filling up the queue.

**Note:** Any stat recorded when the queue is full will be lost.

## Exposing stats to users

In the `UnityEngine.XR.Provider` namespace, use `public static bool
TryGetStat(Experimental.IntegratedSubsystem xrSubsystem, string tag, out float
value)` to get stats registered and updated with your provider:

    
    
    using UnityEngine.XR.Provider;
    using System.Collections.Generic;
    using UnityEngine.Experimental.XR;
    using UnityEngine.Experimental;
    using UnityEngine;
    
    public static class ExampleProviderStats
    {
        public static float GPUFrameTime()
        {
            float tmp;
            XRStats.TryGetStat(GetFirstDisplaySubsystem(), "Example.GPUTime", out tmp);
            return tmp;
        }
    
        public static int DroppedFrameCount()
        {
            float tmp;
            XRStats.TryGetStat(GetFirstDisplaySubsystem(), "Example.DroppedFrame", out tmp);
            return (int)tmp;
        }
    
        public static float MyWorkerThreadStat()
        {
            float tmp;
            XRStats.TryGetStat(GetFirstDisplaySubsystem(), "Example.WorkerThreadStat", out tmp);
            return tmp;
        }
    
        // etc...
        private static IntegratedSubsystem GetFirstDisplaySubsystem()
        {
            List<XRDisplaySubsystem> displays = new List<XRDisplaySubsystem>();
            SubsystemManager.GetInstances(displays);
            if (displays.Count == 0)
            {
                Debug.Log("No display subsystem found.");
                return null;
            }
            return displays[0];
        }
    }
    

Writing public accessor methods such as the example above can help users
acquire stats without the need to sift through provider documentation and find
the subsystem with which stats are registered.

Additionally, some subsystems have predefined stat tags. Your provider can
provide stats for the [predefined stats
APIs](../ScriptReference/XR.XRStats.html) that Unity exposes by registering
subsystem specific stat tags (for example:
`Headers/XR/UnityXRDisplayStats.h`).

[](xrsdk-pre-init-interface.html)

XR SDK PreInit interface

[](UnityServices.html)

Unity Services

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

