[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/low-level-native-plugin-memory-manager-api-reference.html)
  * [中文](/cn/current/Manual/low-level-native-plugin-memory-manager-api-reference.html)
  * [日本語](/ja/current/Manual/low-level-native-plugin-memory-manager-api-reference.html)
  * [한국어](/kr/current/Manual/low-level-native-plugin-memory-manager-api-reference.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/low-level-native-plugin-memory-manager-api-reference.html)
  * [中文](/cn/current/Manual/low-level-native-plugin-memory-manager-api-reference.html)
  * [日本語](/ja/current/Manual/low-level-native-plugin-memory-manager-api-reference.html)
  * [한국어](/kr/current/Manual/low-level-native-plugin-memory-manager-api-reference.html)

  * [Scripting](scripting.html)
  * [Compilation and code reload ](compilation-and-code-reload.html)
  * [Integrating third-party code libraries (plug-ins)](plug-ins.html)
  * [Low-level native plug-in interface](native-plugin-interface.html)
  * [Memory Manager API for low-level native plug-ins](low-level-native-plugin-memory-manager-api.html)
  * IUnityMemoryManager API reference

[](low-level-native-plugin-memory-manager-api.html)

Memory Manager API for low-level native plug-ins

[](LowLevelNativePluginProfiler.html)

Profiling low-level native plug-ins

# IUnityMemoryManager API reference

This pages provides the API reference for the `IUnityMemoryManager` interface.

## CreateAllocator

### Declaration

`UnityAllocator* (UNITY_INTERFACE_API * CreateAllocator)(const char* areaName,
const char* objectName);`

### Parameters

**Parameter** | **Description**  
---|---  
**const char* areaName** | The name for the broad category for this allocator.  
**const char* objectName** | The name for this specific allocator.  
  
### Description

Creates a new Allocator object which can allocate blocks of memory.

## DestroyAllocator

### Declaration

`void(UNITY_INTERFACE_API * DestroyAllocator)(UnityAllocator * allocator);`

### Parameters

**Parameter** | **Description**  
---|---  
**UnityAllocator * allocator** | The allocator to delete.  
  
### Description

Deletes an existing Allocator object.

## Allocate

### Declaration

`void* (UNITY_INTERFACE_API * Allocate)(UnityAllocator * allocator, size_t
size, size_t align, const char* file, int32_t line);`

### Parameters

**Parameter** | **Description**  
---|---  
**UnityAllocator * allocator** | The allocator to use for allocation.  
**size_t size** | How much memory to allocate, in bytes.  
**size_t align** | The alignment of the memory address for the resulting pointer.  
**const char* file** | The path to the source file where the call to make this allocation came from. Use the predefined macro _FILE_ here.  
**int32_t line** | The line number in the source file where the call to make this allocation came from. Use the predefined macro _LINE_ here.  
  
### Description

Allocates a block of memory using an existing allocator. This method returns a
pointer to the newly allocated memory.

## Deallocate

### Declaration

`void(UNITY_INTERFACE_API * Deallocate)(UnityAllocator * allocator, void* ptr,
const char* file, int32_t line);`

### Parameters

**Parameter** | **Description**  
---|---  
**UnityAllocator * allocator** | The allocator to use for deallocation.  
**void* ptr** | The pointer to the memory to be deallocated.  
**const char* file** | The path to the source file where the call to make this deallocation came from. Use the predefined macro _FILE_ here.  
**int32_t line** | The line number in the source file where the call to make this deallocation came from. Use the predefined macro _LINE_ here.  
  
### Description

Deallocates the memory that the specified pointer points to. This doesn’t set
the pointer to NULL.

## Reallocate

### Declaration

`void* (UNITY_INTERFACE_API * Reallocate)(UnityAllocator * allocator, void*
ptr, size_t size, size_t align, const char* file, int32_t line);`

### Parameters

**Parameter** | **Description**  
---|---  
**UnityAllocator * allocator** | The allocator to use for the reallocation operation.  
**void* ptr** | The pointer to the memory to be deallocated.  
**size_t size** | How much memory to allocate, in bytes.  
**size_t align** | The alignment of the memory address for the resulting pointer.  
**const char* file** | The path to the source file where the call to make this reallocation came from. Use the predefined macro _FILE_ here.  
**int32_t line** | The line number in the source file where the call to make this reallocation came from. Use the predefined macro _LINE_ here.  
  
### Description

Reallocates an existing pointer to point to a different block of memory.

## Implementation example

Below is an example implementation of the `IUnityMemoryManager` interface.

    
    
    #include "IUnityInterface.h"
    #include "IUnityMemoryManager.h"
    #include <cstdint>
    
    static IUnityMemoryManager* s_MemoryManager = NULL;
    static UnityAllocator* s_Alloc = NULL;
    
    extern "C" void UNITY_INTERFACE_EXPORT UNITY_INTERFACE_API UnityPluginLoad(IUnityInterfaces * unityInterfaces)
    {
        s_MemoryManager = unityInterfaces->Get<IUnityMemoryManager>();
        if (s_MemoryManager  == NULL)
        return;
    
        // Create an allocator. This allows you to see the allocation root in the profiler when taking snapshots. Under plug-ins-native - Plugin Backend Allocator
       // All memory allocated here also goes under kMemNativePlugin
        s_Alloc = s_MemoryManager->CreateAllocator("plug-ins-native", "Plugin Backend Allocator");
    }
    
    extern "C" void UNITY_INTERFACE_EXPORT UNITY_INTERFACE_API UnityPluginUnload()
    {
        //Free allocator
        s_MemoryManager->DestroyAllocator(s_Alloc);
        s_Alloc = NULL;
        s_MemoryManager = NULL;
    }
    
    void DoMemoryOperations()
    {  
        // Allocate 1KB memory
        void* mem = s_MemoryManager->Allocate(s_Alloc, 1 * 1024, 16, __FILE__, __LINE__);
         // Reallocate the same pointer with 2KB
        mem = s_MemManager->Reallocate(s_Alloc, mem, 2 * 1024, 16, __FILE__, __LINE__);
        // Delete allocated memory
        s_MemoryManager->Deallocate(s_Alloc, mem, __FILE__, __LINE__);
    }
    

## Additional resources

  * [Low-level native plug-in rendering extensions](low-level-native-plugin-rendering-extensions.html)
  * [Low-level native plug-in shader compiler access](low-level-native-plugin-shader-compiler-access.html)
  * [Low-level native plug-in memory manager API](low-level-native-plugin-memory-manager-api.html)

[](low-level-native-plugin-memory-manager-api.html)

Memory Manager API for low-level native plug-ins

[](LowLevelNativePluginProfiler.html)

Profiling low-level native plug-ins

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

