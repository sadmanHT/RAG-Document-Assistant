Persistent Volumes | Kubernetes
[Kubernetes](/)

* [Documentation](/docs/home/)
* [Kubernetes Blog](/blog/)
* [Training](/training/)
* [Careers](/careers/)
* [Partners](/partners/)
* [Community](/community/)
* [Versions](#)

  [Release Information](/releases)
  [v1.36](https://kubernetes.io/docs/concepts/storage/persistent-volumes/)
  [v1.35](https://v1-35.docs.kubernetes.io/docs/concepts/storage/persistent-volumes/)
  [v1.34](https://v1-34.docs.kubernetes.io/docs/concepts/storage/persistent-volumes/)
  [v1.33](https://v1-33.docs.kubernetes.io/docs/concepts/storage/persistent-volumes/)
  [v1.32](https://v1-32.docs.kubernetes.io/docs/concepts/storage/persistent-volumes/)
* [English](#)

  [中文 (Chinese)](/zh-cn/docs/concepts/storage/persistent-volumes/)
  [Français (French)](/fr/docs/concepts/storage/persistent-volumes/)
  [Bahasa Indonesia (Indonesian)](/id/docs/concepts/storage/persistent-volumes/)
  [日本語 (Japanese)](/ja/docs/concepts/storage/persistent-volumes/)
  [한국어 (Korean)](/ko/docs/concepts/storage/persistent-volumes/)
  [Português (Portuguese)](/pt-br/docs/concepts/storage/persistent-volumes/)
  [Español (Spanish)](/es/docs/concepts/storage/persistent-volumes/)
  [Tiếng Việt (Vietnamese)](/vi/docs/concepts/storage/persistent-volumes/)
  বাংলা (Bengali)
  [বাংলা (Bengali)](/bn/) 
  Deutsch (German)
  [Deutsch (German)](/de/) 
  हिन्दी (Hindi)
  [हिन्दी (Hindi)](/hi/) 
  Italiano (Italian)
  [Italiano (Italian)](/it/) 
  Polski (Polish)
  [Polski (Polish)](/pl/) 
  Русский (Russian)
  [Русский (Russian)](/ru/) 
  Українська (Ukrainian)
  [Українська (Ukrainian)](/uk/)

# Persistent Volumes

[English](#)

[বাংলা (Bengali)](/bn/docs/concepts/)
[中文 (Chinese)](/zh-cn/docs/concepts/)
[Français (French)](/fr/docs/concepts/)
[Deutsch (German)](/de/docs/concepts/)
[हिन्दी (Hindi)](/hi/docs/concepts/)
[Bahasa Indonesia (Indonesian)](/id/docs/concepts/)
[Italiano (Italian)](/it/docs/concepts/)
[日本語 (Japanese)](/ja/docs/concepts/)
[한국어 (Korean)](/ko/docs/concepts/)
[Polski (Polish)](/pl/docs/concepts/)
[Português (Portuguese)](/pt-br/docs/concepts/)
[Русский (Russian)](/ru/docs/concepts/)
[Español (Spanish)](/es/docs/concepts/)
[Українська (Ukrainian)](/uk/docs/concepts/)
[Tiếng Việt (Vietnamese)](/vi/docs/concepts/)

* [Kubernetes Documentation](/docs/ "Documentation")
  + [Documentation](/docs/home/ "Kubernetes Documentation")
    - [Available Documentation Versions](/docs/home/supported-doc-versions/)
  + [Getting started](/docs/setup/)
    - [Learning environment](/docs/setup/learning-environment/)
    - [Production environment](/docs/setup/production-environment/)
      * [Container Runtimes](/docs/setup/production-environment/container-runtimes/)
      * [Installing Kubernetes with deployment tools](/docs/setup/production-environment/tools/)
        + [Bootstrapping clusters with kubeadm](/docs/setup/production-environment/tools/kubeadm/)
          - [Installing kubeadm](/docs/setup/production-environment/tools/kubeadm/install-kubeadm/)
          - [Troubleshooting kubeadm](/docs/setup/production-environment/tools/kubeadm/troubleshooting-kubeadm/)
          - [Creating a cluster with kubeadm](/docs/setup/production-environment/tools/kubeadm/create-cluster-kubeadm/)
          - [Customizing components with the kubeadm API](/docs/setup/production-environment/tools/kubeadm/control-plane-flags/)
          - [Options for Highly Available Topology](/docs/setup/production-environment/tools/kubeadm/ha-topology/)
          - [Creating Highly Available Clusters with kubeadm](/docs/setup/production-environment/tools/kubeadm/high-availability/)
          - [Set up a High Availability etcd Cluster with kubeadm](/docs/setup/production-environment/tools/kubeadm/setup-ha-etcd-with-kubeadm/)
          - [Configuring each kubelet in your cluster using kubeadm](/docs/setup/production-environment/tools/kubeadm/kubelet-integration/)
          - [Dual-stack support with kubeadm](/docs/setup/production-environment/tools/kubeadm/dual-stack-support/)
      * [Turnkey Cloud Solutions](/docs/setup/production-environment/turnkey-solutions/)
    - [Best practices](/docs/setup/best-practices/)
      * [Considerations for large clusters](/docs/setup/best-practices/cluster-large/)
      * [Running in multiple zones](/docs/setup/best-practices/multiple-zones/)
      * [Validate node setup](/docs/setup/best-practices/node-conformance/)
      * [Enforcing Pod Security Standards](/docs/setup/best-practices/enforcing-pod-security-standards/)
      * [PKI certificates and requirements](/docs/setup/best-practices/certificates/)
  + [Concepts](/docs/concepts/)
    - [Overview](/docs/concepts/overview/)
      * [Kubernetes Components](/docs/concepts/overview/components/)
      * [Objects In Kubernetes](/docs/concepts/overview/working-with-objects/)
        + [Kubernetes Object Management](/docs/concepts/overview/working-with-objects/object-management/)
        + [Object Names and IDs](/docs/concepts/overview/working-with-objects/names/)
        + [Labels and Selectors](/docs/concepts/overview/working-with-objects/labels/)
        + [Namespaces](/docs/concepts/overview/working-with-objects/namespaces/)
        + [Annotations](/docs/concepts/overview/working-with-objects/annotations/)
        + [Field Selectors](/docs/concepts/overview/working-with-objects/field-selectors/)
        + [Finalizers](/docs/concepts/overview/working-with-objects/finalizers/)
        + [Owners and Dependents](/docs/concepts/overview/working-with-objects/owners-dependents/)
        + [Recommended Labels](/docs/concepts/overview/working-with-objects/common-labels/)
        + [Storage Versions](/docs/concepts/overview/working-with-objects/storage-version/)
      * [The Kubernetes API](/docs/concepts/overview/kubernetes-api/)
      * [The kubectl command-line tool](/docs/concepts/overview/kubectl/)
    - [Cluster Architecture](/docs/concepts/architecture/)
      * [Nodes](/docs/concepts/architecture/nodes/)
      * [Communication between Nodes and the Control Plane](/docs/concepts/architecture/control-plane-node-communication/)
      * [Controllers](/docs/concepts/architecture/controller/)
      * [Leases](/docs/concepts/architecture/leases/)
      * [Cloud Controller Manager](/docs/concepts/architecture/cloud-controller/)
      * [About cgroup v2](/docs/concepts/architecture/cgroups/)
      * [Kubernetes Self-Healing](/docs/concepts/architecture/self-healing/)
      * [Garbage Collection](/docs/concepts/architecture/garbage-collection/)
      * [Mixed Version Proxy](/docs/concepts/architecture/mixed-version-proxy/)
    - [Containers](/docs/concepts/containers/)
      * [Images](/docs/concepts/containers/images/)
      * [Container Environment](/docs/concepts/containers/container-environment/)
      * [Runtime Class](/docs/concepts/containers/runtime-class/)
      * [Container Lifecycle Hooks](/docs/concepts/containers/container-lifecycle-hooks/)
      * [Container Runtime Interface (CRI)](/docs/concepts/containers/cri/)
    - [Workloads](/docs/concepts/workloads/)
      * [Pods](/docs/concepts/workloads/pods/)
        + [Pod Lifecycle](/docs/concepts/workloads/pods/pod-lifecycle/)
        + [Pod Conditions](/docs/concepts/workloads/pods/pod-condition/)
        + [Init Containers](/docs/concepts/workloads/pods/init-containers/)
        + [Sidecar Containers](/docs/concepts/workloads/pods/sidecar-containers/)
        + [Ephemeral Containers](/docs/concepts/workloads/pods/ephemeral-containers/)
        + [Disruptions](/docs/concepts/workloads/pods/disruptions/)
        + [Pod Hostname](/docs/concepts/workloads/pods/pod-hostname/)
        + [Pod Quality of Service Classes](/docs/concepts/workloads/pods/pod-qos/)
        + [Scheduling Group](/docs/concepts/workloads/pods/scheduling-group/)
        + [User Namespaces](/docs/concepts/workloads/pods/user-namespaces/)
        + [Downward API](/docs/concepts/workloads/pods/downward-api/)
        + [Advanced Pod Configuration](/docs/concepts/workloads/pods/advanced-pod-config/)
      * [Workload API](/docs/concepts/workloads/workload-api/)
        + [Pod Group Disruption and Priority](/docs/concepts/workloads/workload-api/disruption-and-priority/)
        + [PodGroup Scheduling Policies](/docs/concepts/workloads/workload-api/policies/)
        + [Topology-Aware Workload Scheduling](/docs/concepts/workloads/workload-api/topology-aware-scheduling/)
      * [Workload Management](/docs/concepts/workloads/controllers/)
        + [Deployments](/docs/concepts/workloads/controllers/deployment/)
        + [ReplicaSet](/docs/concepts/workloads/controllers/replicaset/)
        + [StatefulSets](/docs/concepts/workloads/controllers/statefulset/)
        + [DaemonSet](/docs/concepts/workloads/controllers/daemonset/)
        + [Jobs](/docs/concepts/workloads/controllers/job/)
        + [Automatic Cleanup for Finished Jobs](/docs/concepts/workloads/controllers/ttlafterfinished/)
        + [CronJob](/docs/concepts/workloads/controllers/cron-jobs/)
        + [ReplicationController](/docs/concepts/workloads/controllers/replicationcontroller/)
      * [PodGroup API](/docs/concepts/workloads/podgroup-api/)
        + [PodGroup Lifecycle](/docs/concepts/workloads/podgroup-api/lifecycle/)
      * [Managing Workloads](/docs/concepts/workloads/management/)
      * [Autoscaling Workloads](/docs/concepts/workloads/autoscaling/)
      * [Horizontal Pod Autoscaling](/docs/concepts/workloads/autoscaling/horizontal-pod-autoscale/)
      * [Resource managers](/docs/concepts/workloads/resource-managers/)
      * [Vertical Pod Autoscaling](/docs/concepts/workloads/autoscaling/vertical-pod-autoscale/)
    - [Services, Load Balancing, and Networking](/docs/concepts/services-networking/)
      * [Service](/docs/concepts/services-networking/service/)
      * [Ingress](/docs/concepts/services-networking/ingress/)
      * [Ingress Controllers](/docs/concepts/services-networking/ingress-controllers/)
      * [Gateway API](/docs/concepts/services-networking/gateway/)
      * [EndpointSlices](/docs/concepts/services-networking/endpoint-slices/)
      * [Network Policies](/docs/concepts/services-networking/network-policies/)
      * [DNS for Services and Pods](/docs/concepts/services-networking/dns-pod-service/)
      * [IPv4/IPv6 dual-stack](/docs/concepts/services-networking/dual-stack/)
      * [Topology Aware Routing](/docs/concepts/services-networking/topology-aware-routing/)
      * [Networking on Windows](/docs/concepts/services-networking/windows-networking/)
      * [Service ClusterIP allocation](/docs/concepts/services-networking/cluster-ip-allocation/)
      * [Service Internal Traffic Policy](/docs/concepts/services-networking/service-traffic-policy/)
    - [Storage](/docs/concepts/storage/)
      * [Volumes](/docs/concepts/storage/volumes/)
      * [Persistent Volumes](/docs/concepts/storage/persistent-volumes/)
      * [Projected Volumes](/docs/concepts/storage/projected-volumes/)
      * [Ephemeral Volumes](/docs/concepts/storage/ephemeral-volumes/)
      * [Storage Classes](/docs/concepts/storage/storage-classes/)
      * [Volume Attributes Classes](/docs/concepts/storage/volume-attributes-classes/)
      * [Dynamic Volume Provisioning](/docs/concepts/storage/dynamic-provisioning/)
      * [Volume Snapshots](/docs/concepts/storage/volume-snapshots/)
      * [Volume Snapshot Classes](/docs/concepts/storage/volume-snapshot-classes/)
      * [CSI Volume Cloning](/docs/concepts/storage/volume-pvc-datasource/)
      * [Storage Capacity](/docs/concepts/storage/storage-capacity/)
      * [Node-specific Volume Limits](/docs/concepts/storage/storage-limits/)
      * [Local ephemeral storage](/docs/concepts/storage/ephemeral-storage/)
      * [Volume Health Monitoring](/docs/concepts/storage/volume-health-monitoring/)
      * [Windows Storage](/docs/concepts/storage/windows-storage/)
    - [Configuration](/docs/concepts/configuration/)
      * [ConfigMaps](/docs/concepts/configuration/configmap/)
      * [Secrets](/docs/concepts/configuration/secret/)
      * [Liveness, Readiness, and Startup Probes](/docs/concepts/configuration/liveness-readiness-startup-probes/)
      * [Resource Management for Pods and Containers](/docs/concepts/configuration/manage-resources-containers/)
      * [Organizing Cluster Access Using kubeconfig Files](/docs/concepts/configuration/organize-cluster-access-kubeconfig/)
      * [Resource Management for Windows nodes](/docs/concepts/configuration/windows-resource-management/)
    - [Security](/docs/concepts/security/)
      * [Cloud Native Security](/docs/concepts/security/cloud-native-security/ "Cloud Native Security and Kubernetes")
      * [Pod Security Standards](/docs/concepts/security/pod-security-standards/)
      * [Pod Security Admission](/docs/concepts/security/pod-security-admission/)
      * [Service Accounts](/docs/concepts/security/service-accounts/)
      * [Pod Security Policies](/docs/concepts/security/pod-security-policy/)
      * [Security For Linux Nodes](/docs/concepts/security/linux-security/)
      * [Security For Windows Nodes](/docs/concepts/security/windows-security/)
      * [Controlling Access to the Kubernetes API](/docs/concepts/security/controlling-access/)
      * [Role Based Access Control Good Practices](/docs/concepts/security/rbac-good-practices/)
      * [Good practices for Kubernetes Secrets](/docs/concepts/security/secrets-good-practices/)
      * [Multi-tenancy](/docs/concepts/security/multi-tenancy/)
      * [Hardening Guide - Authentication Mechanisms](/docs/concepts/security/hardening-guide/authentication-mechanisms/)
      * [Hardening Guide - Dynamic Resource Allocation](/docs/concepts/security/hardening-guide/dynamic-resource-allocation/)
      * [Hardening Guide - Scheduler Configuration](/docs/concepts/security/hardening-guide/scheduler/)
      * [Kubernetes API Server Bypass Risks](/docs/concepts/security/api-server-bypass-risks/)
      * [Linux kernel security constraints for Pods and containers](/docs/concepts/security/linux-kernel-security-constraints/)
      * [Security Checklist](/docs/concepts/security/security-checklist/)
      * [Application Security Checklist](/docs/concepts/security/application-security-checklist/)
    - [Policies](/docs/concepts/policy/)
      * [Limit Ranges](/docs/concepts/policy/limit-range/)
      * [Resource Quotas](/docs/concepts/policy/resource-quotas/)
      * [Process ID Limits And Reservations](/docs/concepts/policy/pid-limiting/)
    - [Scheduling, Preemption and Eviction](/docs/concepts/scheduling-eviction/)
      * [Kubernetes Scheduler](/docs/concepts/scheduling-eviction/kube-scheduler/)
      * [Topology-Aware Workload Scheduling](/docs/concepts/scheduling-eviction/topology-aware-scheduling/)
      * [Assigning Pods to Nodes](/docs/concepts/scheduling-eviction/assign-pod-node/)
      * [Pod Overhead](/docs/concepts/scheduling-eviction/pod-overhead/)
      * [Pod Scheduling Readiness](/docs/concepts/scheduling-eviction/pod-scheduling-readiness/)
      * [Pod Topology Spread Constraints](/docs/concepts/scheduling-eviction/topology-spread-constraints/)
      * [Taints and Tolerations](/docs/concepts/scheduling-eviction/taint-and-toleration/)
      * [Scheduling Framework](/docs/concepts/scheduling-eviction/scheduling-framework/)
      * [Dynamic Resource Allocation](/docs/concepts/scheduling-eviction/dynamic-resource-allocation/)
      * [Gang Scheduling](/docs/concepts/scheduling-eviction/gang-scheduling/)
      * [Scheduler Performance Tuning](/docs/concepts/scheduling-eviction/scheduler-perf-tuning/)
      * [PodGroup Scheduling](/docs/concepts/scheduling-eviction/podgroup-scheduling/)
      * [Resource Bin Packing](/docs/concepts/scheduling-eviction/resource-bin-packing/)
      * [Workload-Aware Preemption](/docs/concepts/scheduling-eviction/workload-aware-preemption/)
      * [Pod Priority and Preemption](/docs/concepts/scheduling-eviction/pod-priority-preemption/)
      * [Node-pressure Eviction](/docs/concepts/scheduling-eviction/node-pressure-eviction/)
      * [API-initiated Eviction](/docs/concepts/scheduling-eviction/api-eviction/)
      * [Node Declared Features](/docs/concepts/scheduling-eviction/node-declared-features/)
    - [Cluster Administration](/docs/concepts/cluster-administration/)
      * [Node Shutdowns](/docs/concepts/cluster-administration/node-shutdown/)
      * [Swap memory management](/docs/concepts/cluster-administration/swap-memory-management/)
      * [Node Autoscaling](/docs/concepts/cluster-administration/node-autoscaling/)
      * [Certificates](/docs/concepts/cluster-administration/certificates/)
      * [Cluster Networking](/docs/concepts/cluster-administration/networking/)
      * [Observability](/docs/concepts/cluster-administration/observability/)
      * [Admission Webhook Good Practices](/docs/concepts/cluster-administration/admission-webhooks-good-practices/)
      * [Good practices for Dynamic Resource Allocation as a Cluster Admin](/docs/concepts/cluster-administration/dra/)
      * [Logging Architecture](/docs/concepts/cluster-administration/logging/)
      * [Compatibility Version For Kubernetes Control Plane Components](/docs/concepts/cluster-administration/compatibility-version/)
      * [Metrics For Kubernetes System Components](/docs/concepts/cluster-administration/system-metrics/)
      * [Metrics for Kubernetes Object States](/docs/concepts/cluster-administration/kube-state-metrics/)
      * [System Logs](/docs/concepts/cluster-administration/system-logs/)
      * [Traces For Kubernetes System Components](/docs/concepts/cluster-administration/system-traces/)
      * [Proxies in Kubernetes](/docs/concepts/cluster-administration/proxies/)
      * [API Priority and Fairness](/docs/concepts/cluster-administration/flow-control/)
      * [Installing Addons](/docs/concepts/cluster-administration/addons/)
      * [Coordinated Leader Election](/docs/concepts/cluster-administration/coordinated-leader-election/)
    - [Windows in Kubernetes](/docs/concepts/windows/)
      * [Windows containers in Kubernetes](/docs/concepts/windows/intro/)
      * [Guide for Running Windows Containers in Kubernetes](/docs/concepts/windows/user-guide/)
    - [Extending Kubernetes](/docs/concepts/extend-kubernetes/)
      * [Compute, Storage, and Networking Extensions](/docs/concepts/extend-kubernetes/compute-storage-net/)
        + [Network Plugins](/docs/concepts/extend-kubernetes/compute-storage-net/network-plugins/)
        + [Device Plugins](/docs/concepts/extend-kubernetes/compute-storage-net/device-plugins/)
      * [Extending the Kubernetes API](/docs/concepts/extend-kubernetes/api-extension/)
        + [Custom Resources](/docs/concepts/extend-kubernetes/api-extension/custom-resources/)
        + [Kubernetes API Aggregation Layer](/docs/concepts/extend-kubernetes/api-extension/apiserver-aggregation/)
      * [Operator pattern](/docs/concepts/extend-kubernetes/operator/)
  + [Tasks](/docs/tasks/)
    - [Install Tools](/docs/tasks/tools/)
      * [Install and Set Up kubectl on Linux](/docs/tasks/tools/install-kubectl-linux/)
      * [Install and Set Up kubectl on macOS](/docs/tasks/tools/install-kubectl-macos/)
      * [Install and Set Up kubectl on Windows](/docs/tasks/tools/install-kubectl-windows/)
    - [Administer a Cluster](/docs/tasks/administer-cluster/)
      * [Administration with kubeadm](/docs/tasks/administer-cluster/kubeadm/)
        + [Adding Linux worker nodes](/docs/tasks/administer-cluster/kubeadm/adding-linux-nodes/)
        + [Adding Windows worker nodes](/docs/tasks/administer-cluster/kubeadm/adding-windows-nodes/)
        + [Upgrading kubeadm clusters](/docs/tasks/administer-cluster/kubeadm/kubeadm-upgrade/)
        + [Upgrading Linux nodes](/docs/tasks/administer-cluster/kubeadm/upgrading-linux-nodes/)
        + [Upgrading Windows nodes](/docs/tasks/administer-cluster/kubeadm/upgrading-windows-nodes/)
        + [Configuring a cgroup driver](/docs/tasks/administer-cluster/kubeadm/configure-cgroup-driver/)
        + [Certificate Management with kubeadm](/docs/tasks/administer-cluster/kubeadm/kubeadm-certs/)
        + [Reconfiguring a kubeadm cluster](/docs/tasks/administer-cluster/kubeadm/kubeadm-reconfigure/)
        + [Changing The Kubernetes Package Repository](/docs/tasks/administer-cluster/kubeadm/change-package-repository/)
      * [Overprovision Node Capacity For A Cluster](/docs/tasks/administer-cluster/node-overprovisioning/)
      * [Migrating from dockershim](/docs/tasks/administer-cluster/migrating-from-dockershim/)
        + [Changing the Container Runtime on a Node from Docker Engine to containerd](/docs/tasks/administer-cluster/migrating-from-dockershim/change-runtime-containerd/)
        + [Find Out What Container Runtime is Used on a Node](/docs/tasks/administer-cluster/migrating-from-dockershim/find-out-runtime-you-use/)
        + [Troubleshooting CNI plugin-related errors](/docs/tasks/administer-cluster/migrating-from-dockershim/troubleshooting-cni-plugin-related-errors/)
        + [Check whether dockershim removal affects you](/docs/tasks/administer-cluster/migrating-from-dockershim/check-if-dockershim-removal-affects-you/)
        + [Migrating telemetry and security agents from dockershim](/docs/tasks/administer-cluster/migrating-from-dockershim/migrating-telemetry-and-security-agents/)
      * [Generate Certificates Manually](/docs/tasks/administer-cluster/certificates/)
      * [Manage Memory, CPU, and API Resources](/docs/tasks/administer-cluster/manage-resources/)
        + [Configure Default Memory Requests and Limits for a Namespace](/docs/tasks/administer-cluster/manage-resources/memory-default-namespace/)
        + [Configure Default CPU Requests and Limits for a Namespace](/docs/tasks/administer-cluster/manage-resources/cpu-default-namespace/)
        + [Configure Minimum and Maximum Memory Constraints for a Namespace](/docs/tasks/administer-cluster/manage-resources/memory-constraint-namespace/)
        + [Configure Minimum and Maximum CPU Constraints for a Namespace](/docs/tasks/administer-cluster/manage-resources/cpu-constraint-namespace/)
        + [Configure Memory and CPU Quotas for a Namespace](/docs/tasks/administer-cluster/manage-resources/quota-memory-cpu-namespace/)
        + [Configure a Pod Quota for a Namespace](/docs/tasks/administer-cluster/manage-resources/quota-pod-namespace/)
      * [Install a Network Policy Provider](/docs/tasks/administer-cluster/network-policy-provider/)
        + [Use Antrea for NetworkPolicy](/docs/tasks/administer-cluster/network-policy-provider/antrea-network-policy/)
        + [Use Calico for NetworkPolicy](/docs/tasks/administer-cluster/network-policy-provider/calico-network-policy/)
        + [Use Cilium for NetworkPolicy](/docs/tasks/administer-cluster/network-policy-provider/cilium-network-policy/)
        + [Use Kube-router for NetworkPolicy](/docs/tasks/administer-cluster/network-policy-provider/kube-router-network-policy/)
        + [Romana for NetworkPolicy](/docs/tasks/administer-cluster/network-policy-provider/romana-network-policy/)
        + [Weave Net for NetworkPolicy](/docs/tasks/administer-cluster/network-policy-provider/weave-network-policy/)
      * [Access Clusters Using the Kubernetes API](/docs/tasks/administer-cluster/access-cluster-api/)
      * [Enable Or Disable Feature Gates](/docs/tasks/administer-cluster/configure-feature-gates/)
      * [Advertise Extended Resources for a Node](/docs/tasks/administer-cluster/extended-resource-node/)
      * [Autoscale the DNS Service in a Cluster](/docs/tasks/administer-cluster/dns-horizontal-autoscaling/)
      * [Change the Access Mode of a PersistentVolume to ReadWriteOncePod](/docs/tasks/administer-cluster/change-pv-access-mode-readwriteoncepod/)
      * [Change the default StorageClass](/docs/tasks/administer-cluster/change-default-storage-class/)
      * [Switching from Polling to CRI Event-based Updates to Container Status](/docs/tasks/administer-cluster/switch-to-evented-pleg/)
      * [Change the Reclaim Policy of a PersistentVolume](/docs/tasks/administer-cluster/change-pv-reclaim-policy/)
      * [Cloud Controller Manager Administration](/docs/tasks/administer-cluster/running-cloud-controller/)
      * [Configure a kubelet image credential provider](/docs/tasks/administer-cluster/kubelet-credential-provider/)
      * [Configure Quotas for API Objects](/docs/tasks/administer-cluster/quota-api-object/)
      * [Control CPU Management Policies on the Node](/docs/tasks/administer-cluster/cpu-management-policies/)
      * [Control Memory Management Policies on a Node](/docs/tasks/administer-cluster/memory-manager/)
      * [Control Topology Management Policies on a node](/docs/tasks/administer-cluster/topology-manager/)
      * [Customizing DNS Service](/docs/tasks/administer-cluster/dns-custom-nameservers/)
      * [Debugging DNS Resolution](/docs/tasks/administer-cluster/dns-debugging-resolution/)
      * [Declare Network Policy](/docs/tasks/administer-cluster/declare-network-policy/)
      * [Developing Cloud Controller Manager](/docs/tasks/administer-cluster/developing-cloud-controller-manager/)
      * [Enable Or Disable A Kubernetes API](/docs/tasks/administer-cluster/enable-disable-api/)
      * [Encrypting Confidential Data at Rest](/docs/tasks/administer-cluster/encrypt-data/)
      * [Decrypt Confidential Data that is Already Encrypted at Rest](/docs/tasks/administer-cluster/decrypt-data/)
      * [Guaranteed Scheduling For Critical Add-On Pods](/docs/tasks/administer-cluster/guaranteed-scheduling-critical-addon-pods/)
      * [IP Masquerade Agent User Guide](/docs/tasks/administer-cluster/ip-masq-agent/)
      * [Limit Storage Consumption](/docs/tasks/administer-cluster/limit-storage-consumption/)
      * [Migrate Replicated Control Plane To Use Cloud Controller Manager](/docs/tasks/administer-cluster/controller-manager-leader-migration/)
      * [Operating etcd clusters for Kubernetes](/docs/tasks/administer-cluster/configure-upgrade-etcd/)
      * [Reserve Compute Resources for System Daemons](/docs/tasks/administer-cluster/reserve-compute-resources/)
      * [Running Kubernetes Node Components as a Non-root User](/docs/tasks/administer-cluster/kubelet-in-userns/)
      * [Safely Drain a Node](/docs/tasks/administer-cluster/safely-drain-node/)
      * [Securing a Cluster](/docs/tasks/administer-cluster/securing-a-cluster/)
      * [Harden Dynamic Resource Allocation in Your Cluster](/docs/tasks/administer-cluster/hardening-dra/)
      * [Set Kubelet Parameters Via A Configuration File](/docs/tasks/administer-cluster/kubelet-config-file/)
      * [Share a Cluster with Namespaces](/docs/tasks/administer-cluster/namespaces/)
      * [Upgrade A Cluster](/docs/tasks/administer-cluster/cluster-upgrade/)
      * [Use Cascading Deletion in a Cluster](/docs/tasks/administer-cluster/use-cascading-deletion/)
      * [Using a KMS provider for data encryption](/docs/tasks/administer-cluster/kms-provider/)
      * [Using CoreDNS for Service Discovery](/docs/tasks/administer-cluster/coredns/)
      * [Using NodeLocal DNSCache in Kubernetes Clusters](/docs/tasks/administer-cluster/nodelocaldns/)
      * [Using sysctls in a Kubernetes Cluster](/docs/tasks/administer-cluster/sysctl-cluster/)
      * [Verify Signed Kubernetes Artifacts](/docs/tasks/administer-cluster/verify-signed-artifacts/)
    - [Configure Pods and Containers](/docs/tasks/configure-pod-container/)
      * [Assign Memory Resources to Containers and Pods](/docs/tasks/configure-pod-container/assign-memory-resource/)
      * [Assign CPU Resources to Containers and Pods](/docs/tasks/configure-pod-container/assign-cpu-resource/)
      * [Assign Devices to Pods and Containers](/docs/tasks/configure-pod-container/assign-resources/)
        + [Set Up DRA in a Cluster](/docs/tasks/configure-pod-container/assign-resources/set-up-dra-cluster/)
        + [Allocate Devices to Workloads with DRA](/docs/tasks/configure-pod-container/assign-resources/allocate-devices-dra/)
        + [Access DRA Device Metadata](/docs/tasks/configure-pod-container/assign-resources/access-dra-device-metadata/)
      * [Assign Pod-level CPU and memory resources](/docs/tasks/configure-pod-container/assign-pod-level-resources/)
      * [Configure GMSA for Windows Pods and containers](/docs/tasks/configure-pod-container/configure-gmsa/)
      * [Resize CPU and Memory Resources assigned to Containers](/docs/tasks/configure-pod-container/resize-container-resources/)
      * [Resize CPU and Memory Resources assigned to Pods](/docs/tasks/configure-pod-container/resize-pod-resources/)
      * [Configure RunAsUserName for Windows pods and containers](/docs/tasks/configure-pod-container/configure-runasusername/)
      * [Create a Windows HostProcess Pod](/docs/tasks/configure-pod-container/create-hostprocess-pod/)
      * [Configure Quality of Service for Pods](/docs/tasks/configure-pod-container/quality-service-pod/)
      * [Assign Extended Resources to a Container](/docs/tasks/configure-pod-container/extended-resource/)
      * [Configure a Pod to Use a Volume for Storage](/docs/tasks/configure-pod-container/configure-volume-storage/)
      * [Configure a Pod to Use a Projected Volume for Storage](/docs/tasks/configure-pod-container/configure-projected-volume-storage/)
      * [Configure a Security Context for a Pod or Container](/docs/tasks/configure-pod-container/security-context/)
      * [Configure Service Accounts for Pods](/docs/tasks/configure-pod-container/configure-service-account/)
      * [Pull an Image from a Private Registry](/docs/tasks/configure-pod-container/pull-image-private-registry/)
      * [Configure Liveness, Readiness and Startup Probes](/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/)
      * [Assign Pods to Nodes](/docs/tasks/configure-pod-container/assign-pods-nodes/)
      * [Assign Pods to Nodes using Node Affinity](/docs/tasks/configure-pod-container/assign-pods-nodes-using-node-affinity/)
      * [Configure Pod Initialization](/docs/tasks/configure-pod-container/configure-pod-initialization/)
      * [Attach Handlers to Container Lifecycle Events](/docs/tasks/configure-pod-container/attach-handler-lifecycle-event/)
      * [Configure a Pod to Use a ConfigMap](/docs/tasks/configure-pod-container/configure-pod-configmap/)
      * [Share Process Namespace between Containers in a Pod](/docs/tasks/configure-pod-container/share-process-namespace/)
      * [Use a User Namespace With a Pod](/docs/tasks/configure-pod-container/user-namespaces/)
      * [Use an Image Volume With a Pod](/docs/tasks/configure-pod-container/image-volumes/)
      * [Create static Pods](/docs/tasks/configure-pod-container/static-pod/)
      * [Translate a Docker Compose File to Kubernetes Resources](/docs/tasks/configure-pod-container/translate-compose-kubernetes/)
      * [Enforce Pod Security Standards by Configuring the Built-in Admission Controller](/docs/tasks/configure-pod-container/enforce-standards-admission-controller/)
      * [Enforce Pod Security Standards with Namespace Labels](/docs/tasks/configure-pod-container/enforce-standards-namespace-labels/)
      * [Migrate from PodSecurityPolicy to the Built-In PodSecurity Admission Controller](/docs/tasks/configure-pod-container/migrate-from-psp/)
    - [Monitoring, Logging, and Debugging](/docs/tasks/debug/)
      * [Logging in Kubernetes](/docs/tasks/debug/logging/)
      * [Monitoring in Kubernetes](/docs/tasks/debug/monitoring/)
      * [Troubleshooting Applications](/docs/tasks/debug/debug-application/)
        + [Debug Pods](/docs/tasks/debug/debug-application/debug-pods/)
        + [Debug Services](/docs/tasks/debug/debug-application/debug-service/)
        + [Debug a StatefulSet](/docs/tasks/debug/debug-application/debug-statefulset/)
        + [Determine the Reason for Pod Failure](/docs/tasks/debug/debug-application/determine-reason-pod-failure/)
        + [Debug Init Containers](/docs/tasks/debug/debug-application/debug-init-containers/)
        + [Debug Running Pods](/docs/tasks/debug/debug-application/debug-running-pod/)
        + [Get a Shell to a Running Container](/docs/tasks/debug/debug-application/get-shell-running-container/)
      * [Troubleshooting Clusters](/docs/tasks/debug/debug-cluster/)
        + [Troubleshooting kubectl](/docs/tasks/debug/debug-cluster/troubleshoot-kubectl/)
        + [Resource metrics pipeline](/docs/tasks/debug/debug-cluster/resource-metrics-pipeline/)
        + [Tools for Monitoring Resources](/docs/tasks/debug/debug-cluster/resource-usage-monitoring/)
        + [Monitor Node Health](/docs/tasks/debug/debug-cluster/monitor-node-health/)
        + [Debugging Kubernetes nodes with crictl](/docs/tasks/debug/debug-cluster/crictl/)
        + [Troubleshooting Topology Management](/docs/tasks/debug/debug-cluster/topology/)
        + [Auditing](/docs/tasks/debug/debug-cluster/audit/)
        + [Debugging Kubernetes Nodes With Kubectl](/docs/tasks/debug/debug-cluster/kubectl-node-debug/)
        + [Developing and debugging services locally using telepresence](/docs/tasks/debug/debug-cluster/local-debugging/)
        + [Windows debugging tips](/docs/tasks/debug/debug-cluster/windows/)
    - [Manage Kubernetes Objects](/docs/tasks/manage-kubernetes-objects/)
      * [Declarative Management of Kubernetes Objects Using Configuration Files](/docs/tasks/manage-kubernetes-objects/declarative-config/)
      * [Declarative Management of Kubernetes Objects Using Kustomize](/docs/tasks/manage-kubernetes-objects/kustomization/)
      * [Managing Kubernetes Objects Using Imperative Commands](/docs/tasks/manage-kubernetes-objects/imperative-command/)
      * [Imperative Management of Kubernetes Objects Using Configuration Files](/docs/tasks/manage-kubernetes-objects/imperative-config/)
      * [Update API Objects in Place Using kubectl patch](/docs/tasks/manage-kubernetes-objects/update-api-object-kubectl-patch/)
      * [Migrate Kubernetes Objects Using Storage Version Migration](/docs/tasks/manage-kubernetes-objects/storage-version-migration/)
    - [Managing Secrets](/docs/tasks/configmap-secret/)
      * [Managing Secrets using kubectl](/docs/tasks/configmap-secret/managing-secret-using-kubectl/)
      * [Managing Secrets using Configuration File](/docs/tasks/configmap-secret/managing-secret-using-config-file/)
      * [Managing Secrets using Kustomize](/docs/tasks/configmap-secret/managing-secret-using-kustomize/)
    - [Inject Data Into Applications](/docs/tasks/inject-data-application/)
      * [Define a Command and Arguments for a Container](/docs/tasks/inject-data-application/define-command-argument-container/)
      * [Define Dependent Environment Variables](/docs/tasks/inject-data-application/define-interdependent-environment-variables/)
      * [Define Environment Variables for a Container](/docs/tasks/inject-data-application/define-environment-variable-container/)
      * [Define Environment Variable Values Using An Init Container](/docs/tasks/inject-data-application/define-environment-variable-via-file/)
      * [Expose Pod Information to Containers Through Environment Variables](/docs/tasks/inject-data-application/environment-variable-expose-pod-information/)
      * [Expose Pod Information to Containers Through Files](/docs/tasks/inject-data-application/downward-api-volume-expose-pod-information/)
      * [Distribute Credentials Securely Using Secrets](/docs/tasks/inject-data-application/distribute-credentials-secure/)
    - [Run Applications](/docs/tasks/run-application/)
      * [Run a Stateless Application Using a Deployment](/docs/tasks/run-application/run-stateless-application-deployment/)
      * [Horizontal Manual Scaling for a Deployment](/docs/tasks/run-application/scale-deployment/)
      * [Update a Deployment Without Downtime](/docs/tasks/run-application/update-deployment-rolling/)
      * [Run a Single-Instance Stateful Application](/docs/tasks/run-application/run-single-instance-stateful-application/)
      * [Run a Replicated Stateful Application](/docs/tasks/run-application/run-replicated-stateful-application/)
      * [Scale a StatefulSet](/docs/tasks/run-application/scale-stateful-set/)
      * [Delete a StatefulSet](/docs/tasks/run-application/delete-stateful-set/)
      * [Force Delete StatefulSet Pods](/docs/tasks/run-application/force-delete-stateful-set-pod/)
      * [HorizontalPodAutoscaler Walkthrough](/docs/tasks/run-application/horizontal-pod-autoscale-walkthrough/)
      * [Specifying a Disruption Budget for your Application](/docs/tasks/run-application/configure-pdb/)
      * [Accessing the Kubernetes API from a Pod](/docs/tasks/run-application/access-api-from-pod/)
    - [Run Jobs](/docs/tasks/job/)
      * [Running Automated Tasks with a CronJob](/docs/tasks/job/automated-tasks-with-cron-jobs/)
      * [Coarse Parallel Processing Using a Work Queue](/docs/tasks/job/coarse-parallel-processing-work-queue/)
      * [Fine Parallel Processing Using a Work Queue](/docs/tasks/job/fine-parallel-processing-work-queue/)
      * [Indexed Job for Parallel Processing with Static Work Assignment](/docs/tasks/job/indexed-parallel-processing-static/)
      * [Job with Pod-to-Pod Communication](/docs/tasks/job/job-with-pod-to-pod-communication/)
      * [Parallel Processing using Expansions](/docs/tasks/job/parallel-processing-expansion/)
      * [Handling retriable and non-retriable pod failures with Pod failure policy](/docs/tasks/job/pod-failure-policy/)
    - [Access Applications in a Cluster](/docs/tasks/access-application-cluster/)
      * [Deploy and Access the Kubernetes Dashboard](/docs/tasks/access-application-cluster/web-ui-dashboard/)
      * [Accessing Clusters](/docs/tasks/access-application-cluster/access-cluster/)
      * [Configure Access to Multiple Clusters](/docs/tasks/access-application-cluster/configure-access-multiple-clusters/)
      * [Use Port Forwarding to Access Applications in a Cluster](/docs/tasks/access-application-cluster/port-forward-access-application-cluster/)
      * [Use a Service to Access an Application in a Cluster](/docs/tasks/access-application-cluster/service-access-application-cluster/)
      * [Connect a Frontend to a Backend Using Services](/docs/tasks/access-application-cluster/connecting-frontend-backend/)
      * [Create an External Load Balancer](/docs/tasks/access-application-cluster/create-external-load-balancer/)
      * [List All Container Images Running in a Cluster](/docs/tasks/access-application-cluster/list-all-running-container-images/)
      * [Communicate Between Containers in the Same Pod Using a Shared Volume](/docs/tasks/access-application-cluster/communicate-containers-same-pod-shared-volume/)
      * [Configure DNS for a Cluster](/docs/tasks/access-application-cluster/configure-dns-cluster/)
      * [Access Services Running on Clusters](/docs/tasks/access-application-cluster/access-cluster-services/)
    - [Extend Kubernetes](/docs/tasks/extend-kubernetes/)
      * [Configure the Aggregation Layer](/docs/tasks/extend-kubernetes/configure-aggregation-layer/)
      * [Use Custom Resources](/docs/tasks/extend-kubernetes/custom-resources/)
        + [Extend the Kubernetes API with CustomResourceDefinitions](/docs/tasks/extend-kubernetes/custom-resources/custom-resource-definitions/)
        + [Versions in CustomResourceDefinitions](/docs/tasks/extend-kubernetes/custom-resources/custom-resource-definition-versioning/)
      * [Set up an Extension API Server](/docs/tasks/extend-kubernetes/setup-extension-api-server/)
      * [Configure Multiple Schedulers](/docs/tasks/extend-kubernetes/configure-multiple-schedulers/)
      * [Use an HTTP Proxy to Access the Kubernetes API](/docs/tasks/extend-kubernetes/http-proxy-access-api/)
      * [Use a SOCKS5 Proxy to Access the Kubernetes API](/docs/tasks/extend-kubernetes/socks5-proxy-access-api/)
      * [Set up Konnectivity service](/docs/tasks/extend-kubernetes/setup-konnectivity/)
    - [TLS](/docs/tasks/tls/)
      * [Issue a Certificate for a Kubernetes API Client Using A CertificateSigningRequest](/docs/tasks/tls/certificate-issue-client-csr/)
      * [Configure Certificate Rotation for the Kubelet](/docs/tasks/tls/certificate-rotation/)
      * [Manage TLS Certificates in a Cluster](/docs/tasks/tls/managing-tls-in-a-cluster/)
      * [Manual Rotation of CA Certificates](/docs/tasks/tls/manual-rotation-of-ca-certificates/)
    - [Manage Cluster Daemons](/docs/tasks/manage-daemon/)
      * [Building a Basic DaemonSet](/docs/tasks/manage-daemon/create-daemon-set/)
      * [Perform a Rolling Update on a DaemonSet](/docs/tasks/manage-daemon/update-daemon-set/)
      * [Perform a Rollback on a DaemonSet](/docs/tasks/manage-daemon/rollback-daemon-set/)
      * [Running Pods on Only Some Nodes](/docs/tasks/manage-daemon/pods-some-nodes/)
    - [Networking](/docs/tasks/network/)
      * [Adding entries to Pod /etc/hosts with HostAliases](/docs/tasks/network/customize-hosts-file-for-pods/)
      * [Extend Service IP Ranges](/docs/tasks/network/extend-service-ip-ranges/)
      * [Kubernetes Default ServiceCIDR Reconfiguration](/docs/tasks/network/reconfigure-default-service-ip-ranges/)
      * [Validate IPv4/IPv6 dual-stack](/docs/tasks/network/validate-dual-stack/)
    - [Extend kubectl with plugins](/docs/tasks/extend-kubectl/kubectl-plugins/)
    - [Manage HugePages](/docs/tasks/manage-hugepages/scheduling-hugepages/)
    - [Schedule GPUs](/docs/tasks/manage-gpus/scheduling-gpus/)
  + [Tutorials](/docs/tutorials/)
    - [Hello Minikube](/docs/tutorials/hello-minikube/)
    - [Learn Kubernetes Basics](/docs/tutorials/kubernetes-basics/)
      * [Create a Cluster](/docs/tutorials/kubernetes-basics/create-cluster/)
        + [Using Minikube to Create a Cluster](/docs/tutorials/kubernetes-basics/create-cluster/cluster-intro/)
      * [Deploy an App](/docs/tutorials/kubernetes-basics/deploy-app/)
        + [Using kubectl to Create a Deployment](/docs/tutorials/kubernetes-basics/deploy-app/deploy-intro/)
      * [Explore Your App](/docs/tutorials/kubernetes-basics/explore/)
        + [Viewing Pods and Nodes](/docs/tutorials/kubernetes-basics/explore/explore-intro/)
      * [Expose Your App Publicly](/docs/tutorials/kubernetes-basics/expose/)
        + [Using a Service to Expose Your App](/docs/tutorials/kubernetes-basics/expose/expose-intro/)
      * [Scale Your App](/docs/tutorials/kubernetes-basics/scale/)
        + [Running Multiple Instances of Your App](/docs/tutorials/kubernetes-basics/scale/scale-intro/)
      * [Update Your App](/docs/tutorials/kubernetes-basics/update/)
        + [Performing a Rolling Update](/docs/tutorials/kubernetes-basics/update/update-intro/)
    - [Configuration](/docs/tutorials/configuration/)
      * [Updating Configuration via a ConfigMap](/docs/tutorials/configuration/updating-configuration-via-a-configmap/)
      * [Configuring Redis using a ConfigMap](/docs/tutorials/configuration/configure-redis-using-configmap/)
      * [Adopting Sidecar Containers](/docs/tutorials/configuration/pod-sidecar-containers/)
      * [Configure a Pod to Use a PersistentVolume for Storage](/docs/tutorials/configuration/configure-persistent-volume-storage/)
    - [Security](/docs/tutorials/security/)
      * [Apply Pod Security Standards at the Cluster Level](/docs/tutorials/security/cluster-level-pss/)
      * [Apply Pod Security Standards at the Namespace Level](/docs/tutorials/security/ns-level-pss/)
      * [Restrict a Container's Access to Resources with AppArmor](/docs/tutorials/security/apparmor/)
      * [Restrict a Container's Syscalls with seccomp](/docs/tutorials/security/seccomp/)
    - [Stateless Applications](/docs/tutorials/stateless-application/)
      * [Exposing an External IP Address to Access an Application in a Cluster](/docs/tutorials/stateless-application/expose-external-ip-address/)
      * [Example: Deploying PHP Guestbook application with Redis](/docs/tutorials/stateless-application/guestbook/)
    - [Stateful Applications](/docs/tutorials/stateful-application/)
      * [StatefulSet Basics](/docs/tutorials/stateful-application/basic-stateful-set/)
      * [Example: Deploying WordPress and MySQL with Persistent Volumes](/docs/tutorials/stateful-application/mysql-wordpress-persistent-volume/)
      * [Example: Deploying Cassandra with a StatefulSet](/docs/tutorials/stateful-application/cassandra/)
      * [Running ZooKeeper, A Distributed System Coordinator](/docs/tutorials/stateful-application/zookeeper/)
    - [Cluster Management](/docs/tutorials/cluster-management/)
      * [Running Kubelet in Standalone Mode](/docs/tutorials/cluster-management/kubelet-standalone/)
      * [Configuring swap memory on Kubernetes nodes](/docs/tutorials/cluster-management/provision-swap-memory/)
      * [Install Drivers and Allocate Devices with DRA](/docs/tutorials/cluster-management/install-use-dra/)
      * [Namespaces Walkthrough](/docs/tutorials/cluster-management/namespaces-walkthrough/)
    - [Services](/docs/tutorials/services/)
      * [Connecting Applications with Services](/docs/tutorials/services/connect-applications-service/)
      * [Using Source IP](/docs/tutorials/services/source-ip/)
      * [Explore Termination Behavior for Pods And Their Endpoints](/docs/tutorials/services/pods-and-endpoint-termination-flow/)
  + [Reference](/docs/reference/)
    - [Glossary](/docs/reference/glossary/)
    - [API Overview](/docs/reference/using-api/)
      * [Declarative API Validation](/docs/reference/using-api/declarative-validation/)
      * [Kubernetes API Concepts](/docs/reference/using-api/api-concepts/)
      * [Server-Side Apply](/docs/reference/using-api/server-side-apply/)
      * [Client Libraries](/docs/reference/using-api/client-libraries/)
      * [Common Expression Language in Kubernetes](/docs/reference/using-api/cel/)
      * [Kubernetes Deprecation Policy](/docs/reference/using-api/deprecation-policy/)
      * [Deprecated API Migration Guide](/docs/reference/using-api/deprecation-guide/)
      * [Kubernetes API health endpoints](/docs/reference/using-api/health-checks/)
    - [API Access Control](/docs/reference/access-authn-authz/)
      * [Authenticating](/docs/reference/access-authn-authz/authentication/)
      * [Authenticating with Bootstrap Tokens](/docs/reference/access-authn-authz/bootstrap-tokens/)
      * [Authorization](/docs/reference/access-authn-authz/authorization/)
      * [Using RBAC Authorization](/docs/reference/access-authn-authz/rbac/)
      * [Using Node Authorization](/docs/reference/access-authn-authz/node/)
      * [Webhook Mode](/docs/reference/access-authn-authz/webhook/)
      * [Using ABAC Authorization](/docs/reference/access-authn-authz/abac/)
      * [Admission Control](/docs/reference/access-authn-authz/admission-controllers/ "Admission Control in Kubernetes")
      * [Dynamic Admission Control](/docs/reference/access-authn-authz/extensible-admission-controllers/)
      * [Managing Service Accounts](/docs/reference/access-authn-authz/service-accounts-admin/)
      * [User Impersonation](/docs/reference/access-authn-authz/user-impersonation/)
      * [Certificates and Certificate Signing Requests](/docs/reference/access-authn-authz/certificate-signing-requests/)
      * [Mapping PodSecurityPolicies to Pod Security Standards](/docs/reference/access-authn-authz/psp-to-pod-security-standards/)
      * [Kubelet authentication/authorization](/docs/reference/access-authn-authz/kubelet-authn-authz/)
      * [TLS bootstrapping](/docs/reference/access-authn-authz/kubelet-tls-bootstrapping/)
      * [Manifest-Based Admission Control](/docs/reference/access-authn-authz/manifest-admission-control/)
      * [Mutating Admission Policy](/docs/reference/access-authn-authz/mutating-admission-policy/)
      * [Validating Admission Policy](/docs/reference/access-authn-authz/validating-admission-policy/)
    - [Well-Known Labels, Annotations and Taints](/docs/reference/labels-annotations-taints/)
      * [Audit Annotations](/docs/reference/labels-annotations-taints/audit-annotations/)
    - [Kubernetes API](/docs/reference/kubernetes-api/)
      * [Workload Resources](/docs/reference/kubernetes-api/workload-resources/)
        + [Pod](/docs/reference/kubernetes-api/workload-resources/pod-v1/)
        + [Binding](/docs/reference/kubernetes-api/workload-resources/binding-v1/)
        + [PodTemplate](/docs/reference/kubernetes-api/workload-resources/pod-template-v1/)
        + [PodGroup v1alpha2](/docs/reference/kubernetes-api/workload-resources/pod-group-v1alpha2/)
        + [ReplicationController](/docs/reference/kubernetes-api/workload-resources/replication-controller-v1/)
        + [ReplicaSet](/docs/reference/kubernetes-api/workload-resources/replica-set-v1/)
        + [Deployment](/docs/reference/kubernetes-api/workload-resources/deployment-v1/)
        + [StatefulSet](/docs/reference/kubernetes-api/workload-resources/stateful-set-v1/)
        + [ControllerRevision](/docs/reference/kubernetes-api/workload-resources/controller-revision-v1/)
        + [DaemonSet](/docs/reference/kubernetes-api/workload-resources/daemon-set-v1/)
        + [Job](/docs/reference/kubernetes-api/workload-resources/job-v1/)
        + [CronJob](/docs/reference/kubernetes-api/workload-resources/cron-job-v1/)
        + [HorizontalPodAutoscaler](/docs/reference/kubernetes-api/workload-resources/horizontal-pod-autoscaler-v1/)
        + [HorizontalPodAutoscaler](/docs/reference/kubernetes-api/workload-resources/horizontal-pod-autoscaler-v2/)
        + [PriorityClass](/docs/reference/kubernetes-api/workload-resources/priority-class-v1/)
        + [DeviceTaintRule v1beta2](/docs/reference/kubernetes-api/workload-resources/device-taint-rule-v1beta2/)
        + [ResourceClaim](/docs/reference/kubernetes-api/workload-resources/resource-claim-v1/)
        + [ResourceClaimTemplate](/docs/reference/kubernetes-api/workload-resources/resource-claim-template-v1/)
        + [ResourceSlice](/docs/reference/kubernetes-api/workload-resources/resource-slice-v1/)
        + [Workload v1alpha2](/docs/reference/kubernetes-api/workload-resources/workload-v1alpha2/)
      * [Service Resources](/docs/reference/kubernetes-api/service-resources/)
        + [Service](/docs/reference/kubernetes-api/service-resources/service-v1/)
        + [Endpoints](/docs/reference/kubernetes-api/service-resources/endpoints-v1/)
        + [EndpointSlice](/docs/reference/kubernetes-api/service-resources/endpoint-slice-v1/)
        + [Ingress](/docs/reference/kubernetes-api/service-resources/ingress-v1/)
        + [IngressClass](/docs/reference/kubernetes-api/service-resources/ingress-class-v1/)
      * [Config and Storage Resources](/docs/reference/kubernetes-api/config-and-storage-resources/)
        + [ConfigMap](/docs/reference/kubernetes-api/config-and-storage-resources/config-map-v1/)
        + [Secret](/docs/reference/kubernetes-api/config-and-storage-resources/secret-v1/)
        + [CSIDriver](/docs/reference/kubernetes-api/config-and-storage-resources/csi-driver-v1/)
        + [CSINode](/docs/reference/kubernetes-api/config-and-storage-resources/csi-node-v1/)
        + [CSIStorageCapacity](/docs/reference/kubernetes-api/config-and-storage-resources/csi-storage-capacity-v1/)
        + [PersistentVolumeClaim](/docs/reference/kubernetes-api/config-and-storage-resources/persistent-volume-claim-v1/)
        + [PersistentVolume](/docs/reference/kubernetes-api/config-and-storage-resources/persistent-volume-v1/)
        + [StorageClass](/docs/reference/kubernetes-api/config-and-storage-resources/storage-class-v1/)
        + [StorageVersionMigration v1beta1](/docs/reference/kubernetes-api/config-and-storage-resources/storage-version-migration-v1beta1/)
        + [Volume](/docs/reference/kubernetes-api/config-and-storage-resources/volume/)
        + [VolumeAttachment](/docs/reference/kubernetes-api/config-and-storage-resources/volume-attachment-v1/)
        + [VolumeAttributesClass](/docs/reference/kubernetes-api/config-and-storage-resources/volume-attributes-class-v1/)
      * [Authentication Resources](/docs/reference/kubernetes-api/authentication-resources/)
        + [ServiceAccount](/docs/reference/kubernetes-api/authentication-resources/service-account-v1/)
        + [TokenRequest](/docs/reference/kubernetes-api/authentication-resources/token-request-v1/)
        + [TokenReview](/docs/reference/kubernetes-api/authentication-resources/token-review-v1/)
        + [CertificateSigningRequest](/docs/reference/kubernetes-api/authentication-resources/certificate-signing-request-v1/)
        + [ClusterTrustBundle v1beta1](/docs/reference/kubernetes-api/authentication-resources/cluster-trust-bundle-v1beta1/)
        + [SelfSubjectReview](/docs/reference/kubernetes-api/authentication-resources/self-subject-review-v1/)
        + [PodCertificateRequest v1beta1](/docs/reference/kubernetes-api/authentication-resources/pod-certificate-request-v1beta1/)
      * [Authorization Resources](/docs/reference/kubernetes-api/authorization-resources/)
        + [LocalSubjectAccessReview](/docs/reference/kubernetes-api/authorization-resources/local-subject-access-review-v1/)
        + [SelfSubjectAccessReview](/docs/reference/kubernetes-api/authorization-resources/self-subject-access-review-v1/)
        + [SelfSubjectRulesReview](/docs/reference/kubernetes-api/authorization-resources/self-subject-rules-review-v1/)
        + [SubjectAccessReview](/docs/reference/kubernetes-api/authorization-resources/subject-access-review-v1/)
        + [ClusterRole](/docs/reference/kubernetes-api/authorization-resources/cluster-role-v1/)
        + [ClusterRoleBinding](/docs/reference/kubernetes-api/authorization-resources/cluster-role-binding-v1/)
        + [Role](/docs/reference/kubernetes-api/authorization-resources/role-v1/)
        + [RoleBinding](/docs/reference/kubernetes-api/authorization-resources/role-binding-v1/)
      * [Policy Resources](/docs/reference/kubernetes-api/policy-resources/)
        + [FlowSchema](/docs/reference/kubernetes-api/policy-resources/flow-schema-v1/)
        + [LimitRange](/docs/reference/kubernetes-api/policy-resources/limit-range-v1/)
        + [ResourceQuota](/docs/reference/kubernetes-api/policy-resources/resource-quota-v1/)
        + [NetworkPolicy](/docs/reference/kubernetes-api/policy-resources/network-policy-v1/)
        + [PodDisruptionBudget](/docs/reference/kubernetes-api/policy-resources/pod-disruption-budget-v1/)
        + [PriorityLevelConfiguration](/docs/reference/kubernetes-api/policy-resources/priority-level-configuration-v1/)
        + [ValidatingAdmissionPolicy](/docs/reference/kubernetes-api/policy-resources/validating-admission-policy-v1/)
        + [ValidatingAdmissionPolicyBinding](/docs/reference/kubernetes-api/policy-resources/validating-admission-policy-binding-v1/)
        + [MutatingAdmissionPolicy](/docs/reference/kubernetes-api/policy-resources/mutating-admission-policy-v1/)
        + [MutatingAdmissionPolicyBinding](/docs/reference/kubernetes-api/policy-resources/mutating-admission-policy-binding-v1/)
      * [Extend Resources](/docs/reference/kubernetes-api/extend-resources/)
        + [CustomResourceDefinition](/docs/reference/kubernetes-api/extend-resources/custom-resource-definition-v1/)
        + [DeviceClass](/docs/reference/kubernetes-api/extend-resources/device-class-v1/)
        + [MutatingWebhookConfiguration](/docs/reference/kubernetes-api/extend-resources/mutating-webhook-configuration-v1/)
        + [ValidatingWebhookConfiguration](/docs/reference/kubernetes-api/extend-resources/validating-webhook-configuration-v1/)
      * [Cluster Resources](/docs/reference/kubernetes-api/cluster-resources/)
        + [APIService](/docs/reference/kubernetes-api/cluster-resources/api-service-v1/)
        + [ComponentStatus](/docs/reference/kubernetes-api/cluster-resources/component-status-v1/)
        + [Event](/docs/reference/kubernetes-api/cluster-resources/event-v1/)
        + [IPAddress](/docs/reference/kubernetes-api/cluster-resources/ip-address-v1/)
        + [Lease](/docs/reference/kubernetes-api/cluster-resources/lease-v1/)
        + [LeaseCandidate v1beta1](/docs/reference/kubernetes-api/cluster-resources/lease-candidate-v1beta1/)
        + [Namespace](/docs/reference/kubernetes-api/cluster-resources/namespace-v1/)
        + [Node](/docs/reference/kubernetes-api/cluster-resources/node-v1/)
        + [RuntimeClass](/docs/reference/kubernetes-api/cluster-resources/runtime-class-v1/)
        + [ResourcePoolStatusRequest v1alpha3](/docs/reference/kubernetes-api/cluster-resources/resource-pool-status-request-v1alpha3/)
        + [ServiceCIDR](/docs/reference/kubernetes-api/cluster-resources/service-cidr-v1/)
      * [Common Definitions](/docs/reference/kubernetes-api/common-definitions/)
        + [DeleteOptions](/docs/reference/kubernetes-api/common-definitions/delete-options/)
        + [LabelSelector](/docs/reference/kubernetes-api/common-definitions/label-selector/)
        + [ListMeta](/docs/reference/kubernetes-api/common-definitions/list-meta/)
        + [LocalObjectReference](/docs/reference/kubernetes-api/common-definitions/local-object-reference/)
        + [NodeSelectorRequirement](/docs/reference/kubernetes-api/common-definitions/node-selector-requirement/)
        + [ObjectFieldSelector](/docs/reference/kubernetes-api/common-definitions/object-field-selector/)
        + [ObjectMeta](/docs/reference/kubernetes-api/common-definitions/object-meta/)
        + [ObjectReference](/docs/reference/kubernetes-api/common-definitions/object-reference/)
        + [Patch](/docs/reference/kubernetes-api/common-definitions/patch/)
        + [Quantity](/docs/reference/kubernetes-api/common-definitions/quantity/)
        + [ResourceFieldSelector](/docs/reference/kubernetes-api/common-definitions/resource-field-selector/)
        + [Status](/docs/reference/kubernetes-api/common-definitions/status/)
        + [TypedLocalObjectReference](/docs/reference/kubernetes-api/common-definitions/typed-local-object-reference/)
      * [Common Parameters](/docs/reference/kubernetes-api/common-parameters/common-parameters/)
    - [Instrumentation](/docs/reference/instrumentation/)
      * [Service Level Indicator Metrics](/docs/reference/instrumentation/slis/ "Kubernetes Component SLI Metrics")
      * [CRI Pod & Container Metrics](/docs/reference/instrumentation/cri-pod-container-metrics/)
      * [Native Histograms](/docs/reference/instrumentation/native-histograms/ "Native Histogram Support for Kubernetes Metrics")
      * [Node metrics data](/docs/reference/instrumentation/node-metrics/)
      * [Understand Pressure Stall Information (PSI) Metrics](/docs/reference/instrumentation/understand-psi-metrics/)
      * [Kubernetes z-pages](/docs/reference/instrumentation/zpages/)
      * [Kubernetes Metrics Reference](/docs/reference/instrumentation/metrics/)
    - [Kubernetes Issues and Security](/docs/reference/issues-security/)
      * [Kubernetes Issue Tracker](/docs/reference/issues-security/issues/)
      * [Kubernetes Security and Disclosure Information](/docs/reference/issues-security/security/)
      * [CVE feed](/docs/reference/issues-security/official-cve-feed/ "Official CVE Feed")
    - [Node Reference Information](/docs/reference/node/)
      * [Kubelet Checkpoint API](/docs/reference/node/kubelet-checkpoint-api/)
      * [Linux Kernel Version Requirements](/docs/reference/node/kernel-version-requirements/)
      * [Articles on dockershim Removal and on Using CRI-compatible Runtimes](/docs/reference/node/topics-on-dockershim-and-cri-compatible-runtimes/)
      * [Kubelet Pod Info gRPC API](/docs/reference/node/kubelet-pod-info-grpc-api/)
      * [Node Labels Populated By The Kubelet](/docs/reference/node/node-labels/)
      * [Kubelet Sync Loop](/docs/reference/node/kubelet-sync-loop/)
      * [Local Files And Paths Used By The Kubelet](/docs/reference/node/kubelet-files/)
      * [Kubelet Configuration Directory Merging](/docs/reference/node/kubelet-config-directory-merging/)
      * [Kubelet Device Manager API Versions](/docs/reference/node/device-plugin-api-versions/)
      * [Kubelet Systemd Watchdog](/docs/reference/node/systemd-watchdog/)
      * [Node Status](/docs/reference/node/node-status/)
      * [Seccomp and Kubernetes](/docs/reference/node/seccomp/)
      * [Linux Node Swap Behaviors](/docs/reference/node/swap-behavior/)
    - [Networking Reference](/docs/reference/networking/)
      * [Protocols for Services](/docs/reference/networking/service-protocols/)
      * [Ports and Protocols](/docs/reference/networking/ports-and-protocols/)
      * [Virtual IPs and Service Proxies](/docs/reference/networking/virtual-ips/)
    - [Setup tools](/docs/reference/setup-tools/)
      * [Kubeadm](/docs/reference/setup-tools/kubeadm/)
        + [kubeadm init](/docs/reference/setup-tools/kubeadm/kubeadm-init/)
        + [kubeadm join](/docs/reference/setup-tools/kubeadm/kubeadm-join/)
        + [kubeadm upgrade](/docs/reference/setup-tools/kubeadm/kubeadm-upgrade/)
        + [kubeadm upgrade phases](/docs/reference/setup-tools/kubeadm/kubeadm-upgrade-phase/)
        + [kubeadm config](/docs/reference/setup-tools/kubeadm/kubeadm-config/)
        + [kubeadm reset](/docs/reference/setup-tools/kubeadm/kubeadm-reset/)
        + [kubeadm token](/docs/reference/setup-tools/kubeadm/kubeadm-token/)
        + [kubeadm version](/docs/reference/setup-tools/kubeadm/kubeadm-version/)
        + [kubeadm alpha](/docs/reference/setup-tools/kubeadm/kubeadm-alpha/)
        + [kubeadm certs](/docs/reference/setup-tools/kubeadm/kubeadm-certs/)
        + [kubeadm init phase](/docs/reference/setup-tools/kubeadm/kubeadm-init-phase/)
        + [kubeadm join phase](/docs/reference/setup-tools/kubeadm/kubeadm-join-phase/)
        + [kubeadm kubeconfig](/docs/reference/setup-tools/kubeadm/kubeadm-kubeconfig/)
        + [kubeadm reset phase](/docs/reference/setup-tools/kubeadm/kubeadm-reset-phase/)
        + [Implementation details](/docs/reference/setup-tools/kubeadm/implementation-details/)
    - [Command line tool (kubectl)](/docs/reference/kubectl/)
      * [Introduction to kubectl](/docs/reference/kubectl/introduction/)
      * [kubectl Quick Reference](/docs/reference/kubectl/quick-reference/)
      * [kubectl reference](/docs/reference/kubectl/generated/)
        + [kubectl](/docs/reference/kubectl/generated/kubectl/)
        + [kubectl annotate](/docs/reference/kubectl/generated/kubectl_annotate/)
        + [kubectl api-resources](/docs/reference/kubectl/generated/kubectl_api-resources/)
        + [kubectl api-versions](/docs/reference/kubectl/generated/kubectl_api-versions/)
        + [kubectl apply](/docs/reference/kubectl/generated/kubectl_apply/)
          - [kubectl apply edit-last-applied](/docs/reference/kubectl/generated/kubectl_apply/kubectl_apply_edit-last-applied/)
          - [kubectl apply set-last-applied](/docs/reference/kubectl/generated/kubectl_apply/kubectl_apply_set-last-applied/)
          - [kubectl apply view-last-applied](/docs/reference/kubectl/generated/kubectl_apply/kubectl_apply_view-last-applied/)
        + [kubectl attach](/docs/reference/kubectl/generated/kubectl_attach/)
        + [kubectl auth](/docs/reference/kubectl/generated/kubectl_auth/)
          - [kubectl auth can-i](/docs/reference/kubectl/generated/kubectl_auth/kubectl_auth_can-i/)
          - [kubectl auth reconcile](/docs/reference/kubectl/generated/kubectl_auth/kubectl_auth_reconcile/)
          - [kubectl auth whoami](/docs/reference/kubectl/generated/kubectl_auth/kubectl_auth_whoami/)
        + [kubectl autoscale](/docs/reference/kubectl/generated/kubectl_autoscale/)
        + [kubectl certificate](/docs/reference/kubectl/generated/kubectl_certificate/)
          - [kubectl certificate approve](/docs/reference/kubectl/generated/kubectl_certificate/kubectl_certificate_approve/)
          - [kubectl certificate deny](/docs/reference/kubectl/generated/kubectl_certificate/kubectl_certificate_deny/)
        + [kubectl cluster-info](/docs/reference/kubectl/generated/kubectl_cluster-info/)
          - [kubectl cluster-info dump](/docs/reference/kubectl/generated/kubectl_cluster-info/kubectl_cluster-info_dump/)
        + [kubectl completion](/docs/reference/kubectl/generated/kubectl_completion/)
        + [kubectl config](/docs/reference/kubectl/generated/kubectl_config/)
          - [kubectl config current-context](/docs/reference/kubectl/generated/kubectl_config/kubectl_config_current-context/)
          - [kubectl config delete-cluster](/docs/reference/kubectl/generated/kubectl_config/kubectl_config_delete-cluster/)
          - [kubectl config delete-context](/docs/reference/kubectl/generated/kubectl_config/kubectl_config_delete-context/)
          - [kubectl config delete-user](/docs/reference/kubectl/generated/kubectl_config/kubectl_config_delete-user/)
          - [kubectl config get-clusters](/docs/reference/kubectl/generated/kubectl_config/kubectl_config_get-clusters/)
          - [kubectl config get-contexts](/docs/reference/kubectl/generated/kubectl_config/kubectl_config_get-contexts/)
          - [kubectl config get-users](/docs/reference/kubectl/generated/kubectl_config/kubectl_config_get-users/)
          - [kubectl config rename-context](/docs/reference/kubectl/generated/kubectl_config/kubectl_config_rename-context/)
          - [kubectl config set](/docs/reference/kubectl/generated/kubectl_config/kubectl_config_set/)
          - [kubectl config set-cluster](/docs/reference/kubectl/generated/kubectl_config/kubectl_config_set-cluster/)
          - [kubectl config set-context](/docs/reference/kubectl/generated/kubectl_config/kubectl_config_set-context/)
          - [kubectl config set-credentials](/docs/reference/kubectl/generated/kubectl_config/kubectl_config_set-credentials/)
          - [kubectl config unset](/docs/reference/kubectl/generated/kubectl_config/kubectl_config_unset/)
          - [kubectl config use-context](/docs/reference/kubectl/generated/kubectl_config/kubectl_config_use-context/)
          - [kubectl config view](/docs/reference/kubectl/generated/kubectl_config/kubectl_config_view/)
        + [kubectl cordon](/docs/reference/kubectl/generated/kubectl_cordon/)
        + [kubectl cp](/docs/reference/kubectl/generated/kubectl_cp/)
        + [kubectl create](/docs/reference/kubectl/generated/kubectl_create/)
          - [kubectl create clusterrole](/docs/reference/kubectl/generated/kubectl_create/kubectl_create_clusterrole/)
          - [kubectl create clusterrolebinding](/docs/reference/kubectl/generated/kubectl_create/kubectl_create_clusterrolebinding/)
          - [kubectl create configmap](/docs/reference/kubectl/generated/kubectl_create/kubectl_create_configmap/)
          - [kubectl create cronjob](/docs/reference/kubectl/generated/kubectl_create/kubectl_create_cronjob/)
          - [kubectl create deployment](/docs/reference/kubectl/generated/kubectl_create/kubectl_create_deployment/)
          - [kubectl create ingress](/docs/reference/kubectl/generated/kubectl_create/kubectl_create_ingress/)
          - [kubectl create job](/docs/reference/kubectl/generated/kubectl_create/kubectl_create_job/)
          - [kubectl create namespace](/docs/reference/kubectl/generated/kubectl_create/kubectl_create_namespace/)
          - [kubectl create poddisruptionbudget](/docs/reference/kubectl/generated/kubectl_create/kubectl_create_poddisruptionbudget/)
          - [kubectl create priorityclass](/docs/reference/kubectl/generated/kubectl_create/kubectl_create_priorityclass/)
          - [kubectl create quota](/docs/reference/kubectl/generated/kubectl_create/kubectl_create_quota/)
          - [kubectl create role](/docs/reference/kubectl/generated/kubectl_create/kubectl_create_role/)
          - [kubectl create rolebinding](/docs/reference/kubectl/generated/kubectl_create/kubectl_create_rolebinding/)
          - [kubectl create secret](/docs/reference/kubectl/generated/kubectl_create/kubectl_create_secret/)
          - [kubectl create secret docker-registry](/docs/reference/kubectl/generated/kubectl_create/kubectl_create_secret_docker-registry/)
          - [kubectl create secret generic](/docs/reference/kubectl/generated/kubectl_create/kubectl_create_secret_generic/)
          - [kubectl create secret tls](/docs/reference/kubectl/generated/kubectl_create/kubectl_create_secret_tls/)
          - [kubectl create service](/docs/reference/kubectl/generated/kubectl_create/kubectl_create_service/)
          - [kubectl create service clusterip](/docs/reference/kubectl/generated/kubectl_create/kubectl_create_service_clusterip/)
          - [kubectl create service externalname](/docs/reference/kubectl/generated/kubectl_create/kubectl_create_service_externalname/)
          - [kubectl create service loadbalancer](/docs/reference/kubectl/generated/kubectl_create/kubectl_create_service_loadbalancer/)
          - [kubectl create service nodeport](/docs/reference/kubectl/generated/kubectl_create/kubectl_create_service_nodeport/)
          - [kubectl create serviceaccount](/docs/reference/kubectl/generated/kubectl_create/kubectl_create_serviceaccount/)
          - [kubectl create token](/docs/reference/kubectl/generated/kubectl_create/kubectl_create_token/)
        + [kubectl debug](/docs/reference/kubectl/generated/kubectl_debug/)
        + [kubectl delete](/docs/reference/kubectl/generated/kubectl_delete/)
        + [kubectl describe](/docs/reference/kubectl/generated/kubectl_describe/)
        + [kubectl diff](/docs/reference/kubectl/generated/kubectl_diff/)
        + [kubectl drain](/docs/reference/kubectl/generated/kubectl_drain/)
        + [kubectl edit](/docs/reference/kubectl/generated/kubectl_edit/)
        + [kubectl events](/docs/reference/kubectl/generated/kubectl_events/)
        + [kubectl exec](/docs/reference/kubectl/generated/kubectl_exec/)
        + [kubectl explain](/docs/reference/kubectl/generated/kubectl_explain/)
        + [kubectl expose](/docs/reference/kubectl/generated/kubectl_expose/)
        + [kubectl get](/docs/reference/kubectl/generated/kubectl_get/)
        + [kubectl kuberc](/docs/reference/kubectl/generated/kubectl_kuberc/)
          - [kubectl kuberc set](/docs/reference/kubectl/generated/kubectl_kuberc/kubectl_kuberc_set/)
          - [kubectl kuberc view](/docs/reference/kubectl/generated/kubectl_kuberc/kubectl_kuberc_view/)
        + [kubectl kustomize](/docs/reference/kubectl/generated/kubectl_kustomize/)
        + [kubectl label](/docs/reference/kubectl/generated/kubectl_label/)
        + [kubectl logs](/docs/reference/kubectl/generated/kubectl_logs/)
        + [kubectl options](/docs/reference/kubectl/generated/kubectl_options/)
        + [kubectl patch](/docs/reference/kubectl/generated/kubectl_patch/)
        + [kubectl plugin](/docs/reference/kubectl/generated/kubectl_plugin/)
          - [kubectl plugin list](/docs/reference/kubectl/generated/kubectl_plugin/kubectl_plugin_list/)
        + [kubectl port-forward](/docs/reference/kubectl/generated/kubectl_port-forward/)
        + [kubectl proxy](/docs/reference/kubectl/generated/kubectl_proxy/)
        + [kubectl replace](/docs/reference/kubectl/generated/kubectl_replace/)
        + [kubectl rollout](/docs/reference/kubectl/generated/kubectl_rollout/)
          - [kubectl rollout history](/docs/reference/kubectl/generated/kubectl_rollout/kubectl_rollout_history/)
          - [kubectl rollout pause](/docs/reference/kubectl/generated/kubectl_rollout/kubectl_rollout_pause/)
          - [kubectl rollout restart](/docs/reference/kubectl/generated/kubectl_rollout/kubectl_rollout_restart/)
          - [kubectl rollout resume](/docs/reference/kubectl/generated/kubectl_rollout/kubectl_rollout_resume/)
          - [kubectl rollout status](/docs/reference/kubectl/generated/kubectl_rollout/kubectl_rollout_status/)
          - [kubectl rollout undo](/docs/reference/kubectl/generated/kubectl_rollout/kubectl_rollout_undo/)
        + [kubectl run](/docs/reference/kubectl/generated/kubectl_run/)
        + [kubectl scale](/docs/reference/kubectl/generated/kubectl_scale/)
        + [kubectl set](/docs/reference/kubectl/generated/kubectl_set/)
          - [kubectl set env](/docs/reference/kubectl/generated/kubectl_set/kubectl_set_env/)
          - [kubectl set image](/docs/reference/kubectl/generated/kubectl_set/kubectl_set_image/)
          - [kubectl set resources](/docs/reference/kubectl/generated/kubectl_set/kubectl_set_resources/)
          - [kubectl set selector](/docs/reference/kubectl/generated/kubectl_set/kubectl_set_selector/)
          - [kubectl set serviceaccount](/docs/reference/kubectl/generated/kubectl_set/kubectl_set_serviceaccount/)
          - [kubectl set subject](/docs/reference/kubectl/generated/kubectl_set/kubectl_set_subject/)
        + [kubectl taint](/docs/reference/kubectl/generated/kubectl_taint/)
        + [kubectl top](/docs/reference/kubectl/generated/kubectl_top/)
          - [kubectl top node](/docs/reference/kubectl/generated/kubectl_top/kubectl_top_node/)
          - [kubectl top pod](/docs/reference/kubectl/generated/kubectl_top/kubectl_top_pod/)
        + [kubectl uncordon](/docs/reference/kubectl/generated/kubectl_uncordon/)
        + [kubectl version](/docs/reference/kubectl/generated/kubectl_version/)
        + [kubectl wait](/docs/reference/kubectl/generated/kubectl_wait/)
      * [kubectl Commands](/docs/reference/kubectl/kubectl-cmds/)
      * [kubectl](/docs/reference/kubectl/kubectl/)
      * [JSONPath Support](/docs/reference/kubectl/jsonpath/)
      * [kubectl for Docker Users](/docs/reference/kubectl/docker-cli-to-kubectl/)
      * [kubectl Usage Conventions](/docs/reference/kubectl/conventions/)
      * [Kubectl user preferences (kuberc)](/docs/reference/kubectl/kuberc/)
    - [Encodings](/docs/reference/encodings/)
      * [KYAML Reference](/docs/reference/encodings/kyaml/)
    - [Component tools](/docs/reference/command-line-tools-reference/)
      * [Feature Gates](/docs/reference/command-line-tools-reference/feature-gates/)
      * [Feature Gates (removed)](/docs/reference/command-line-tools-reference/feature-gates-removed/)
      * [kube-apiserver](/docs/reference/command-line-tools-reference/kube-apiserver/)
      * [kube-controller-manager](/docs/reference/command-line-tools-reference/kube-controller-manager/)
      * [kube-proxy](/docs/reference/command-line-tools-reference/kube-proxy/)
      * [kube-scheduler](/docs/reference/command-line-tools-reference/kube-scheduler/)
      * [kubelet](/docs/reference/command-line-tools-reference/kubelet/)
    - [Debug cluster](/docs/reference/debug-cluster/)
      * [Flow control](/docs/reference/debug-cluster/flow-control/)
    - [Configuration APIs](/docs/reference/config-api/)
      * [Client Authentication (v1)](/docs/reference/config-api/client-authentication.v1/)
      * [Client Authentication (v1beta1)](/docs/reference/config-api/client-authentication.v1beta1/)
      * [Event Rate Limit Configuration (v1alpha1)](/docs/reference/config-api/apiserver-eventratelimit.v1alpha1/)
      * [Image Policy API (v1alpha1)](/docs/reference/config-api/imagepolicy.v1alpha1/)
      * [kube-apiserver Admission (v1)](/docs/reference/config-api/apiserver-admission.v1/)
      * [kube-apiserver Audit Configuration (v1)](/docs/reference/config-api/apiserver-audit.v1/)
      * [kube-apiserver Configuration (v1)](/docs/reference/config-api/apiserver-config.v1/)
      * [kube-apiserver Configuration (v1alpha1)](/docs/reference/config-api/apiserver-config.v1alpha1/)
      * [kube-apiserver Configuration (v1beta1)](/docs/reference/config-api/apiserver-config.v1beta1/)
      * [kube-controller-manager Configuration (v1alpha1)](/docs/reference/config-api/kube-controller-manager-config.v1alpha1/)
      * [kube-proxy Configuration (v1alpha1)](/docs/reference/config-api/kube-proxy-config.v1alpha1/)
      * [kube-scheduler Configuration (v1)](/docs/reference/config-api/kube-scheduler-config.v1/)
      * [kubeadm Configuration (v1beta3)](/docs/reference/config-api/kubeadm-config.v1beta3/)
      * [kubeadm Configuration (v1beta4)](/docs/reference/config-api/kubeadm-config.v1beta4/)
      * [kubeconfig (v1)](/docs/reference/config-api/kubeconfig.v1/)
      * [Kubelet Configuration (v1)](/docs/reference/config-api/kubelet-config.v1/)
      * [Kubelet Configuration (v1alpha1)](/docs/reference/config-api/kubelet-config.v1alpha1/)
      * [Kubelet Configuration (v1beta1)](/docs/reference/config-api/kubelet-config.v1beta1/)
      * [Kubelet CredentialProvider (v1)](/docs/reference/config-api/kubelet-credentialprovider.v1/)
      * [kuberc (v1alpha1)](/docs/reference/config-api/kuberc.v1alpha1/)
      * [kuberc (v1beta1)](/docs/reference/config-api/kuberc.v1beta1/)
      * [WebhookAdmission Configuration (v1)](/docs/reference/config-api/apiserver-webhookadmission.v1/)
    - [External APIs](/docs/reference/external-api/)
      * [Kubernetes Custom Metrics (v1beta2)](/docs/reference/external-api/custom-metrics.v1beta2/)
      * [Kubernetes External Metrics (v1beta1)](/docs/reference/external-api/external-metrics.v1beta1/)
      * [Kubernetes Metrics (v1beta1)](/docs/reference/external-api/metrics.v1beta1/)
    - [Scheduling](/docs/reference/scheduling/)
      * [Scheduler Configuration](/docs/reference/scheduling/config/)
      * [Scheduling Policies](/docs/reference/scheduling/policies/)
    - [Other Tools](/docs/reference/tools/)
  + [Contribute](/docs/contribute/ "Contribute to Kubernetes")
    - [Contribute to Kubernetes Documentation](/docs/contribute/docs/)
    - [Contributing to Kubernetes blogs](/docs/contribute/blog/)
      * [Submitting articles to Kubernetes blogs](/docs/contribute/blog/article-submission/)
      * [Blog guidelines](/docs/contribute/blog/guidelines/)
      * [Blog article mirroring](/docs/contribute/blog/article-mirroring/)
      * [Post-release communications](/docs/contribute/blog/release-comms/)
      * [Helping as a blog writing buddy](/docs/contribute/blog/writing-buddy/)
    - [Suggesting content improvements](/docs/contribute/suggesting-improvements/)
    - [Contributing new content](/docs/contribute/new-content/)
      * [Opening a pull request](/docs/contribute/new-content/open-a-pr/)
      * [Previewing locally](/docs/contribute/new-content/preview-locally/)
      * [Documenting for a release](/docs/contribute/new-content/new-features/ "Documenting a feature for a release")
      * [Case studies](/docs/contribute/new-content/case-studies/ "Submitting case studies")
    - [Reviewing changes](/docs/contribute/review/)
      * [Reviewing pull requests](/docs/contribute/review/reviewing-prs/)
      * [For approvers and reviewers](/docs/contribute/review/for-approvers/ "Reviewing for approvers and reviewers")
    - [Localizing Kubernetes documentation](/docs/contribute/localization/)
    - [Participating in SIG Docs](/docs/contribute/participate/)
      * [Roles and responsibilities](/docs/contribute/participate/roles-and-responsibilities/)
      * [Issue Wranglers](/docs/contribute/participate/issue-wrangler/)
      * [PR wranglers](/docs/contribute/participate/pr-wranglers/)
    - [Documentation style overview](/docs/contribute/style/)
      * [Content guide](/docs/contribute/style/content-guide/ "Documentation Content Guide")
      * [Style guide](/docs/contribute/style/style-guide/ "Documentation Style Guide")
      * [Diagram guide](/docs/contribute/style/diagram-guide/ "Diagram Guide")
      * [Writing a new topic](/docs/contribute/style/write-new-topic/)
      * [Page content types](/docs/contribute/style/page-content-types/)
      * [Content organization](/docs/contribute/style/content-organization/)
      * [Custom Hugo Shortcodes](/docs/contribute/style/hugo-shortcodes/)
    - [Updating Reference Documentation](/docs/contribute/generate-ref-docs/)
      * [Quickstart](/docs/contribute/generate-ref-docs/quickstart/ "Reference Documentation Quickstart")
      * [Contributing to the Upstream Kubernetes Code](/docs/contribute/generate-ref-docs/contribute-upstream/)
      * [Generating Reference Documentation for the Kubernetes API](/docs/contribute/generate-ref-docs/kubernetes-api/)
      * [Generating Reference Documentation for kubectl Commands](/docs/contribute/generate-ref-docs/kubectl/)
      * [Generating Reference Documentation for Metrics](/docs/contribute/generate-ref-docs/metrics-reference/)
      * [Generating Reference Pages for Kubernetes Components and Tools](/docs/contribute/generate-ref-docs/kubernetes-components/)
    - [Advanced contributing](/docs/contribute/advanced/)
    - [Viewing Site Analytics](/docs/contribute/analytics/)
  + [Docs smoke test page](/docs/test/)

[PersistentVolume API reference](https://kubernetes.io/docs/reference/kubernetes-api/config-and-storage-resources/persistent-volume-v1/) [PersistentVolumeClaim API reference](https://kubernetes.io/docs/reference/kubernetes-api/config-and-storage-resources/persistent-volume-claim-v1/)
 [Edit this page](https://github.com/kubernetes/website/edit/main/content/en/docs/concepts/storage/persistent-volumes.md)
 [Create child page](https://github.com/kubernetes/website/new/main/content/en/docs/concepts/storage/persistent-volumes.md?filename=change-me.md&value=---%0Atitle%3A+%22Long+Page+Title%22%0AlinkTitle%3A+%22Short+Nav+Title%22%0Aweight%3A+100%0Adescription%3A+%3E-%0A+++++Page+description+for+heading+and+indexes.%0A---%0A%0A%23%23+Heading%0A%0AEdit+this+template+to+create+your+new+page.%0A%0A%2A+Give+it+a+good+name%2C+ending+in+%60.md%60+-+e.g.+%60getting-started.md%60%0A%2A+Edit+the+%22front+matter%22+section+at+the+top+of+the+page+%28weight+controls+how+its+ordered+amongst+other+pages+in+the+same+directory%3B+lowest+number+first%29.%0A%2A+Add+a+good+commit+message+at+the+bottom+of+the+page+%28%3C80+characters%3B+use+the+extended+description+field+for+more+detail%29.%0A%2A+Create+a+new+branch+so+you+can+preview+your+new+file+and+request+a+review+via+Pull+Request.%0A)
 [Create an issue](https://github.com/kubernetes/website/issues/new?title=Persistent%20Volumes)
 [Print entire section](https://kubernetes.io/docs/concepts/storage/_print/)

* [Introduction](#introduction)
* [Lifecycle of a volume and claim](#lifecycle-of-a-volume-and-claim)
  + [Provisioning](#provisioning)
  + [Binding](#binding)
  + [Using](#using)
  + [Storage Object in Use Protection](#storage-object-in-use-protection)
  + [Reclaiming](#reclaiming)
  + [PersistentVolume deletion protection finalizer](#persistentvolume-deletion-protection-finalizer)
  + [Reserving a PersistentVolume](#reserving-a-persistentvolume)
  + [Expanding Persistent Volumes Claims](#expanding-persistent-volumes-claims)
* [Types of Persistent Volumes](#types-of-persistent-volumes)
* [Persistent Volumes](#persistent-volumes)
  + [Capacity](#capacity)
  + [Volume Mode](#volume-mode)
  + [Access Modes](#access-modes)
  + [Class](#class)
  + [Reclaim Policy](#reclaim-policy)
  + [Mount Options](#mount-options)
  + [Node Affinity](#node-affinity)
  + [Phase](#phase)
* [PersistentVolumeClaims](#persistentvolumeclaims)
  + [Access Modes](#access-modes-1)
  + [Volume Modes](#volume-modes)
  + [Volume Name](#volume-name)
  + [Resources](#resources)
  + [Selector](#selector)
  + [Class](#class-1)
  + [Unused PVC tracking](#unused-pvc-tracking)
* [Claims As Volumes](#claims-as-volumes)
  + [A Note on Namespaces](#a-note-on-namespaces)
  + [PersistentVolumes typed `hostPath`](#persistentvolumes-typed-hostpath)
* [Raw Block Volume Support](#raw-block-volume-support)
  + [PersistentVolume using a Raw Block Volume](#persistent-volume-using-a-raw-block-volume)
  + [PersistentVolumeClaim requesting a Raw Block Volume](#persistent-volume-claim-requesting-a-raw-block-volume)
  + [Pod specification adding Raw Block Device path in container](#pod-specification-adding-raw-block-device-path-in-container)
  + [Binding Block Volumes](#binding-block-volumes)
* [Volume Snapshot and Restore Volume from Snapshot Support](#volume-snapshot-and-restore-volume-from-snapshot-support)
  + [Create a PersistentVolumeClaim from a Volume Snapshot](#create-persistent-volume-claim-from-volume-snapshot)
* [Volume Cloning](#volume-cloning)
  + [Create PersistentVolumeClaim from an existing PVC](#create-persistent-volume-claim-from-an-existing-pvc)
* [Volume populators and data sources](#volume-populators-and-data-sources)
* [Cross namespace data sources](#cross-namespace-data-sources)
* [Data source references](#data-source-references)
  + [Using volume populators](#using-volume-populators)
  + [Using a cross-namespace volume data source](#using-a-cross-namespace-volume-data-source)
* [Writing Portable Configuration](#writing-portable-configuration)
* [What's next](#what-s-next)
  + [API references](#reference)

1. [Kubernetes Documentation](https://kubernetes.io/docs/)
2. [Concepts](https://kubernetes.io/docs/concepts/)
3. [Storage](https://kubernetes.io/docs/concepts/storage/)
4. [Persistent Volumes](https://kubernetes.io/docs/concepts/storage/persistent-volumes/)

# Persistent Volumes

This document describes *persistent volumes* in Kubernetes. Familiarity with
[volumes](/docs/concepts/storage/volumes/), [StorageClasses](/docs/concepts/storage/storage-classes/)
and [VolumeAttributesClasses](/docs/concepts/storage/volume-attributes-classes/) is suggested.

## Introduction

Managing storage is a distinct problem from managing compute instances.
The PersistentVolume subsystem provides an API for users and administrators
that abstracts details of how storage is provided from how it is consumed.
To do this, we introduce two new API resources: PersistentVolume and PersistentVolumeClaim.

A *PersistentVolume* (PV) is a piece of storage in the cluster that has been
provisioned by an administrator or dynamically provisioned using
[Storage Classes](/docs/concepts/storage/storage-classes/). It is a resource in
the cluster just like a node is a cluster resource. PVs are volume plugins like
Volumes, but have a lifecycle independent of any individual Pod that uses the PV.
This API object captures the details of the implementation of the storage, be that
NFS, iSCSI, or a cloud-provider-specific storage system.

A *PersistentVolumeClaim* (PVC) is a request for storage by a user. It is similar
to a Pod. Pods consume node resources and PVCs consume PV resources. Pods can
request specific levels of resources (CPU and Memory). Claims can request specific
size and access modes (e.g., they can be mounted ReadWriteOnce, ReadOnlyMany,
ReadWriteMany, or ReadWriteOncePod, see [AccessModes](#access-modes)).

While PersistentVolumeClaims allow a user to consume abstract storage resources,
it is common that users need PersistentVolumes with varying properties, such as
performance, for different problems. Cluster administrators need to be able to
offer a variety of PersistentVolumes that differ in more ways than size and access
modes, without exposing users to the details of how those volumes are implemented.
For these needs, there is the *StorageClass* resource.

See the [detailed walkthrough with working examples](/docs/tutorials/configuration/configure-persistent-volume-storage/).

## Lifecycle of a volume and claim

PVs are resources in the cluster. PVCs are requests for those resources and also act
as claim checks to the resource. The interaction between PVs and PVCs follows this lifecycle:

### Provisioning

There are two ways PVs may be provisioned: statically or dynamically.

#### Static

A cluster administrator creates a number of PVs. They carry the details of the
real storage, which is available for use by cluster users. They exist in the
Kubernetes API and are available for consumption.

#### Dynamic

When none of the static PVs the administrator created match a user's PersistentVolumeClaim,
the cluster may try to dynamically provision a volume specially for the PVC.
This provisioning is based on StorageClasses: the PVC must request a
[storage class](/docs/concepts/storage/storage-classes/) and
the administrator must have created and configured that class for dynamic
provisioning to occur. Claims that request the class `""` effectively disable
dynamic provisioning for themselves.

To enable dynamic storage provisioning based on storage class, the cluster administrator
needs to enable the `DefaultStorageClass`
[admission controller](/docs/reference/access-authn-authz/admission-controllers/#defaultstorageclass)
on the API server. This can be done, for example, by ensuring that `DefaultStorageClass` is
among the comma-delimited, ordered list of values for the `--enable-admission-plugins` flag of
the API server component. For more information on API server command-line flags,
check [kube-apiserver](/docs/reference/command-line-tools-reference/kube-apiserver/) documentation.

### Binding

A user creates, or in the case of dynamic provisioning, has already created,
a PersistentVolumeClaim with a specific amount of storage requested and with
certain access modes. A control loop in the control plane watches for new PVCs, finds
a matching PV (if possible), and binds them together. If a PV was dynamically
provisioned for a new PVC, the loop will always bind that PV to the PVC. Otherwise,
the user will always get at least what they asked for, but the volume may be in
excess of what was requested. Once bound, PersistentVolumeClaim binds are exclusive,
regardless of how they were bound. A PVC to PV binding is a one-to-one mapping,
using a ClaimRef which is a bi-directional binding between the PersistentVolume
and the PersistentVolumeClaim.

Claims will remain unbound indefinitely if a matching volume does not exist.
Claims will be bound as matching volumes become available. For example, a
cluster provisioned with many 50Gi PVs would not match a PVC requesting 100Gi.
The PVC can be bound when a 100Gi PV is added to the cluster.

### Using

Pods use claims as volumes. The cluster inspects the claim to find the bound
volume and mounts that volume for a Pod. For volumes that support multiple
access modes, the user specifies which mode is desired when using their claim
as a volume in a Pod.

Once a user has a claim and that claim is bound, the bound PV belongs to the
user for as long as they need it. Users schedule Pods and access their claimed
PVs by including a `persistentVolumeClaim` section in a Pod's `volumes` block.
See [Claims As Volumes](#claims-as-volumes) for more details on this.

### Storage Object in Use Protection

The purpose of the Storage Object in Use Protection feature is to ensure that
PersistentVolumeClaims (PVCs) in active use by a Pod and PersistentVolume (PVs)
that are bound to PVCs are not removed from the system, as this may result in data loss.

#### Note:

PVC is in active use by a Pod when a Pod object exists that is using the PVC.

If a user deletes a PVC in active use by a Pod, the PVC is not removed immediately.
PVC removal is postponed until the PVC is no longer actively used by any Pods. Also,
if an admin deletes a PV that is bound to a PVC, the PV is not removed immediately.
PV removal is postponed until the PV is no longer bound to a PVC.

You can see that a PVC is protected when the PVC's status is `Terminating` and the
`Finalizers` list includes `kubernetes.io/pvc-protection`:

```
kubectl describe pvc hostpath
Name:          hostpath
Namespace:     default
StorageClass:  example-hostpath
Status:        Terminating
Volume:
Labels:        <none>
Annotations:   volume.beta.kubernetes.io/storage-class=example-hostpath
               volume.beta.kubernetes.io/storage-provisioner=example.com/hostpath
Finalizers:    [kubernetes.io/pvc-protection]
...
```

You can see that a PV is protected when the PV's status is `Terminating` and
the `Finalizers` list includes `kubernetes.io/pv-protection` too:

```
kubectl describe pv task-pv-volume
Name:            task-pv-volume
Labels:          type=local
Annotations:     <none>
Finalizers:      [kubernetes.io/pv-protection]
StorageClass:    standard
Status:          Terminating
Claim:
Reclaim Policy:  Delete
Access Modes:    RWO
Capacity:        1Gi
Message:
Source:
    Type:          HostPath (bare host directory volume)
    Path:          /tmp/data
    HostPathType:
Events:            <none>
```

### Reclaiming

When a user is done with their volume, they can delete the PVC objects from the
API that allows reclamation of the resource. The reclaim policy for a PersistentVolume
tells the cluster what to do with the volume after it has been released of its claim.
Currently, volumes can either be Retained, Recycled, or Deleted.

#### Retain

The `Retain` reclaim policy allows for manual reclamation of the resource.
When the PersistentVolumeClaim is deleted, the PersistentVolume still exists
and the volume is considered "released". But it is not yet available for
another claim because the previous claimant's data remains on the volume.
An administrator can manually reclaim the volume with the following steps.

1. Delete the PersistentVolume. The associated storage asset in external infrastructure
   still exists after the PV is deleted.
2. Manually clean up the data on the associated storage asset accordingly.
3. Manually delete the associated storage asset.

If you want to reuse the same storage asset, create a new PersistentVolume with
the same storage asset definition.

#### Delete

For volume plugins that support the `Delete` reclaim policy, deletion removes
both the PersistentVolume object from Kubernetes, as well as the associated
storage asset in the external infrastructure. Volumes that were dynamically provisioned
inherit the [reclaim policy of their StorageClass](#reclaim-policy), which
defaults to `Delete`. The administrator should configure the StorageClass
according to users' expectations; otherwise, the PV must be edited or
patched after it is created. See
[Change the Reclaim Policy of a PersistentVolume](/docs/tasks/administer-cluster/change-pv-reclaim-policy/).

#### Recycle

#### Warning:

The `Recycle` reclaim policy is deprecated. Instead, the recommended approach
is to use dynamic provisioning.

If supported by the underlying volume plugin, the `Recycle` reclaim policy performs
a basic scrub (`rm -rf /thevolume/*`) on the volume and makes it available again for a new claim.

However, an administrator can configure a custom recycler Pod template using
the Kubernetes controller manager command line arguments as described in the
[reference](/docs/reference/command-line-tools-reference/kube-controller-manager/).
The custom recycler Pod template must contain a `volumes` specification, as
shown in the example below:

```
apiVersion: v1
kind: Pod
metadata:
  name: pv-recycler
  namespace: default
spec:
  restartPolicy: Never
  volumes:
  - name: vol
    hostPath:
      path: /any/path/it/will/be/replaced
  containers:
  - name: pv-recycler
    image: "registry.k8s.io/busybox"
    command: ["/bin/sh", "-c", "test -e /scrub && rm -rf /scrub/..?* /scrub/.[!.]* /scrub/*  && test -z \"$(ls -A /scrub)\" || exit 1"]
    volumeMounts:
    - name: vol
      mountPath: /scrub
```

However, the particular path specified in the custom recycler Pod template in the
`volumes` part is replaced with the particular path of the volume that is being recycled.

### PersistentVolume deletion protection finalizer

FEATURE STATE:
`Kubernetes v1.33 [stable]`(enabled by default)

Finalizers can be added on a PersistentVolume to ensure that PersistentVolumes
having `Delete` reclaim policy are deleted only after the backing storage are deleted.

The finalizer `external-provisioner.volume.kubernetes.io/finalizer`(introduced
in v1.31) is added to both dynamically provisioned and statically provisioned
CSI volumes.

The finalizer `kubernetes.io/pv-controller`(introduced in v1.31) is added to
dynamically provisioned in-tree plugin volumes and skipped for statically
provisioned in-tree plugin volumes.

The following is an example of dynamically provisioned in-tree plugin volume:

```
kubectl describe pv pvc-74a498d6-3929-47e8-8c02-078c1ece4d78
Name:            pvc-74a498d6-3929-47e8-8c02-078c1ece4d78
Labels:          <none>
Annotations:     kubernetes.io/createdby: vsphere-volume-dynamic-provisioner
                 pv.kubernetes.io/bound-by-controller: yes
                 pv.kubernetes.io/provisioned-by: kubernetes.io/vsphere-volume
Finalizers:      [kubernetes.io/pv-protection kubernetes.io/pv-controller]
StorageClass:    vcp-sc
Status:          Bound
Claim:           default/vcp-pvc-1
Reclaim Policy:  Delete
Access Modes:    RWO
VolumeMode:      Filesystem
Capacity:        1Gi
Node Affinity:   <none>
Message:
Source:
    Type:               vSphereVolume (a Persistent Disk resource in vSphere)
    VolumePath:         [vsanDatastore] d49c4a62-166f-ce12-c464-020077ba5d46/kubernetes-dynamic-pvc-74a498d6-3929-47e8-8c02-078c1ece4d78.vmdk
    FSType:             ext4
    StoragePolicyName:  vSAN Default Storage Policy
Events:                 <none>
```

The finalizer `external-provisioner.volume.kubernetes.io/finalizer` is added for CSI volumes.
The following is an example:

```
Name:            pvc-2f0bab97-85a8-4552-8044-eb8be45cf48d
Labels:          <none>
Annotations:     pv.kubernetes.io/provisioned-by: csi.vsphere.vmware.com
Finalizers:      [kubernetes.io/pv-protection external-provisioner.volume.kubernetes.io/finalizer]
StorageClass:    fast
Status:          Bound
Claim:           demo-app/nginx-logs
Reclaim Policy:  Delete
Access Modes:    RWO
VolumeMode:      Filesystem
Capacity:        200Mi
Node Affinity:   <none>
Message:
Source:
    Type:              CSI (a Container Storage Interface (CSI) volume source)
    Driver:            csi.vsphere.vmware.com
    FSType:            ext4
    VolumeHandle:      44830fa8-79b4-406b-8b58-621ba25353fd
    ReadOnly:          false
    VolumeAttributes:      storage.kubernetes.io/csiProvisionerIdentity=1648442357185-8081-csi.vsphere.vmware.com
                           type=vSphere CNS Block Volume
Events:                <none>
```

When the `CSIMigration{provider}` feature flag is enabled for a specific in-tree volume plugin,
the `kubernetes.io/pv-controller` finalizer is replaced by the
`external-provisioner.volume.kubernetes.io/finalizer` finalizer.

The finalizers ensure that the PV object is removed only after the volume is deleted
from the storage backend provided the reclaim policy of the PV is `Delete`. This
also ensures that the volume is deleted from storage backend irrespective of the
order of deletion of PV and PVC.

### Reserving a PersistentVolume

The control plane can [bind PersistentVolumeClaims to matching PersistentVolumes](#binding)
in the cluster. However, if you want a PVC to bind to a specific PV, you need to pre-bind them.

By specifying a PersistentVolume in a PersistentVolumeClaim, you declare a binding
between that specific PV and PVC. If the PersistentVolume exists and has not reserved
PersistentVolumeClaims through its `claimRef` field, then the PersistentVolume and
PersistentVolumeClaim will be bound.

The binding happens regardless of some volume matching criteria, including node affinity.
The control plane still checks that [storage class](/docs/concepts/storage/storage-classes/),
access modes, and requested storage size are valid.

```
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: foo-pvc
  namespace: foo
spec:
  storageClassName: "" # Empty string must be explicitly set otherwise default StorageClass will be set
  volumeName: foo-pv
  ...
```

This method does not guarantee any binding privileges to the PersistentVolume.
If other PersistentVolumeClaims could use the PV that you specify, you first
need to reserve that storage volume. Specify the relevant PersistentVolumeClaim
in the `claimRef` field of the PV so that other PVCs can not bind to it.

```
apiVersion: v1
kind: PersistentVolume
metadata:
  name: foo-pv
spec:
  storageClassName: ""
  claimRef:
    name: foo-pvc
    namespace: foo
  ...
```

This is useful if you want to consume PersistentVolumes that have their `persistentVolumeReclaimPolicy` set
to `Retain`, including cases where you are reusing an existing PV.

### Expanding Persistent Volumes Claims

FEATURE STATE:
`Kubernetes v1.24 [stable]`

Support for expanding PersistentVolumeClaims (PVCs) is enabled by default. You can expand
the following types of volumes:

* [csi](/docs/concepts/storage/volumes/#csi "The Container Storage Interface (CSI) defines a standard interface to expose storage systems to containers.") (including some CSI migrated
  volume types)
* flexVolume (deprecated)
* portworxVolume (deprecated)

You can only expand a PVC if its storage class's `allowVolumeExpansion` field is set to true.

```
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: example-vol-default
provisioner: vendor-name.example/magicstorage
parameters:
  resturl: "http://192.168.10.100:8080"
  restuser: ""
  secretNamespace: ""
  secretName: ""
allowVolumeExpansion: true
```

To request a larger volume for a PVC, edit the PVC object and specify a larger
size. This triggers expansion of the volume that backs the underlying PersistentVolume. A
new PersistentVolume is never created to satisfy the claim. Instead, an existing volume is resized.

#### Warning:

Directly editing the size of a PersistentVolume can prevent an automatic resize of that volume.
If you edit the capacity of a PersistentVolume, and then edit the `.spec` of a matching
PersistentVolumeClaim to make the size of the PersistentVolumeClaim match the PersistentVolume,
then no storage resize happens.
The Kubernetes control plane will see that the desired state of both resources matches,
conclude that the backing volume size has been manually
increased and that no resize is necessary.

#### CSI Volume expansion

FEATURE STATE:
`Kubernetes v1.24 [stable]`

Support for expanding CSI volumes is enabled by default but it also requires a
specific CSI driver to support volume expansion. Refer to documentation of the
specific CSI driver for more information.

#### Resizing a volume containing a file system

You can only resize volumes containing a file system if the file system is XFS, Ext3, or Ext4.

When a volume contains a file system, the file system is only resized when a new Pod is using
the PersistentVolumeClaim in `ReadWrite` mode. File system expansion is either done when a Pod is starting up
or when a Pod is running and the underlying file system supports online expansion.

FlexVolumes (deprecated since Kubernetes v1.23) allow resize if the driver is configured with the
`RequiresFSResize` capability to `true`. The FlexVolume can be resized on Pod restart.

#### Resizing an in-use PersistentVolumeClaim

FEATURE STATE:
`Kubernetes v1.24 [stable]`

In this case, you don't need to delete and recreate a Pod or deployment that is using an existing PVC.
Any in-use PVC automatically becomes available to its Pod as soon as its file system has been expanded.
This feature has no effect on PVCs that are not in use by a Pod or deployment. You must create a Pod that
uses the PVC before the expansion can complete.

Similar to other volume types - FlexVolume volumes can also be expanded when in-use by a Pod.

#### Note:

FlexVolume resize is possible only when the underlying driver supports resize.

#### Recovering from Failure when Expanding Volumes

If a user specifies a new size that is too big to be satisfied by underlying
storage system, expansion of PVC will be continuously retried until user or
cluster administrator takes some action. This can be undesirable and hence
Kubernetes provides following methods of recovering from such failures.

* [Manually with Cluster Administrator access](#recovery-methods-0)
* [By requesting expansion to smaller size](#recovery-methods-1)

If expanding underlying storage fails, the cluster administrator can manually
recover the Persistent Volume Claim (PVC) state and cancel the resize requests.
Otherwise, the resize requests are continuously retried by the controller without
administrator intervention.

1. Mark the PersistentVolume(PV) that is bound to the PersistentVolumeClaim(PVC)
   with `Retain` reclaim policy.
2. Delete the PVC. Since PV has `Retain` reclaim policy - we will not lose any data
   when we recreate the PVC.
3. Delete the `claimRef` entry from PV specs, so as new PVC can bind to it.
   This should make the PV `Available`.
4. Re-create the PVC with smaller size than PV and set `volumeName` field of the
   PVC to the name of the PV. This should bind new PVC to existing PV.
5. Don't forget to restore the reclaim policy of the PV.

If expansion has failed for a PVC, you can retry expansion with a
smaller size than the previously requested value. To request a new expansion attempt with a
smaller proposed size, edit `.spec.resources` for that PVC and choose a value that is less than the
value you previously tried.
This is useful if expansion to a higher value did not succeed because of capacity constraint.
If that has happened, or you suspect that it might have, you can retry expansion by specifying a
size that is within the capacity limits of underlying storage provider. You can monitor status of
resize operation by watching `.status.allocatedResourceStatuses` and events on the PVC.

Note that,
although you can specify a lower amount of storage than what was requested previously,
the new value must still be higher than `.status.capacity`.
Kubernetes does not support shrinking a PVC to less than its current size.

## Types of Persistent Volumes

PersistentVolume types are implemented as plugins. Kubernetes currently supports the following plugins:

* [`csi`](/docs/concepts/storage/volumes/#csi) - Container Storage Interface (CSI)
* [`fc`](/docs/concepts/storage/volumes/#fc) - Fibre Channel (FC) storage
* [`hostPath`](/docs/concepts/storage/volumes/#hostpath) - HostPath volume
  (for single node testing only; WILL NOT WORK in a multi-node cluster;
  consider using `local` volume instead)
* [`iscsi`](/docs/concepts/storage/volumes/#iscsi) - iSCSI (SCSI over IP) storage
* [`local`](/docs/concepts/storage/volumes/#local) - local storage devices
  mounted on nodes.
* [`nfs`](/docs/concepts/storage/volumes/#nfs) - Network File System (NFS) storage

The following types of PersistentVolume are deprecated but still available.
If you are using these volume types except for `flexVolume`, `cephfs` and `rbd`,
please install corresponding CSI drivers.

* [`awsElasticBlockStore`](/docs/concepts/storage/volumes/#awselasticblockstore) - AWS Elastic Block Store (EBS)
  (**migration on by default** starting v1.23)
* [`azureDisk`](/docs/concepts/storage/volumes/#azuredisk) - Azure Disk
  (**migration on by default** starting v1.23)
* [`azureFile`](/docs/concepts/storage/volumes/#azurefile) - Azure File
  (**migration on by default** starting v1.24)
* [`cinder`](/docs/concepts/storage/volumes/#cinder) - Cinder (OpenStack block storage)
  (**migration on by default** starting v1.21)
* [`flexVolume`](/docs/concepts/storage/volumes/#flexvolume) - FlexVolume
  (**deprecated** starting v1.23, no migration plan and no plan to remove support)
* [`gcePersistentDisk`](/docs/concepts/storage/volumes/#gcePersistentDisk) - GCE Persistent Disk
  (**migration on by default** starting v1.23)
* [`portworxVolume`](/docs/concepts/storage/volumes/#portworxvolume) - Portworx volume
  (**migration on by default** starting v1.31)
* [`vsphereVolume`](/docs/concepts/storage/volumes/#vspherevolume) - vSphere VMDK volume
  (**migration on by default** starting v1.25)

Older versions of Kubernetes also supported the following in-tree PersistentVolume types:

* [`cephfs`](/docs/concepts/storage/volumes/#cephfs)
  (**not available** starting v1.31)
* `flocker` - Flocker storage.
  (**not available** starting v1.25)
* `glusterfs` - GlusterFS storage.
  (**not available** starting v1.26)
* `photonPersistentDisk` - Photon controller persistent disk.
  (**not available** starting v1.15)
* `quobyte` - Quobyte volume.
  (**not available** starting v1.25)
* [`rbd`](/docs/concepts/storage/volumes/#rbd) - Rados Block Device (RBD) volume
  (**not available** starting v1.31)
* `scaleIO` - ScaleIO volume.
  (**not available** starting v1.21)
* `storageos` - StorageOS volume.
  (**not available** starting v1.25)

## Persistent Volumes

Each PV contains a spec and status, which is the specification and status of the volume.
The name of a PersistentVolume object must be a valid
[DNS subdomain name](/docs/concepts/overview/working-with-objects/names/#dns-subdomain-names).

```
apiVersion: v1
kind: PersistentVolume
metadata:
  name: pv0003
spec:
  capacity:
    storage: 5Gi
  volumeMode: Filesystem
  accessModes:
    - ReadWriteOnce
  persistentVolumeReclaimPolicy: Recycle
  storageClassName: slow
  mountOptions:
    - hard
    - nfsvers=4.1
  nfs:
    path: /tmp
    server: 172.17.0.2
```

#### Note:

Helper programs relating to the volume type may be required for consumption of
a PersistentVolume within a cluster. In this example, the PersistentVolume is
of type NFS and the helper program /sbin/mount.nfs is required to support the
mounting of NFS filesystems.

### Capacity

Generally, a PV will have a specific storage capacity. This is set using the PV's
`capacity` attribute which is a [Quantity](/docs/reference/glossary/?all=true#term-quantity "A whole-number representation of small or large numbers using SI suffixes.") value.

Currently, storage size is the only resource that can be set or requested.
Future attributes may include IOPS, throughput, etc.

### Volume Mode

FEATURE STATE:
`Kubernetes v1.18 [stable]`

Kubernetes supports two `volumeModes` of PersistentVolumes: `Filesystem` and `Block`.

`volumeMode` is an optional API parameter.
`Filesystem` is the default mode used when `volumeMode` parameter is omitted.

A volume with `volumeMode: Filesystem` is *mounted* into Pods into a directory. If the volume
is backed by a block device and the device is empty, Kubernetes creates a filesystem
on the device before mounting it for the first time.

You can set the value of `volumeMode` to `Block` to use a volume as a raw block device.
Such volume is presented into a Pod as a block device, without any filesystem on it.
This mode is useful to provide a Pod the fastest possible way to access a volume, without
any filesystem layer between the Pod and the volume. On the other hand, the application
running in the Pod must know how to handle a raw block device.
See [Raw Block Volume Support](#raw-block-volume-support)
for an example on how to use a volume with `volumeMode: Block` in a Pod.

### Access Modes

A PersistentVolume can be mounted on a host in any way supported by the resource
provider. As shown in the table below, providers will have different capabilities
and each PV's access modes are set to the specific modes supported by that particular
volume. For example, NFS can support multiple read/write clients, but a specific
NFS PV might be exported on the server as read-only. Each PV gets its own set of
access modes describing that specific PV's capabilities.

The access modes are:

`ReadWriteOnce`
:   the volume can be mounted as read-write by a single node. ReadWriteOnce access
    mode still can allow multiple pods to access (read from or write to) that volume when the pods are
    running on the same node. For single pod access, please see ReadWriteOncePod.

`ReadOnlyMany`
:   the volume can be mounted as read-only by many nodes.

`ReadWriteMany`
:   the volume can be mounted as read-write by many nodes.

`ReadWriteOncePod`
:   FEATURE STATE:
    `Kubernetes v1.29 [stable]`

    the volume can be mounted as read-write by a single Pod. Use ReadWriteOncePod
    access mode if you want to ensure that only one pod across the whole cluster can
    read that PVC or write to it.

#### Note:

The `ReadWriteOncePod` access mode is only supported for
[CSI](/docs/concepts/storage/volumes/#csi "The Container Storage Interface (CSI) defines a standard interface to expose storage systems to containers.") volumes and Kubernetes version
1.22+. To use this feature you will need to update the following
[CSI sidecars](https://kubernetes-csi.github.io/docs/sidecar-containers.html)
to these versions or greater:

* [csi-provisioner:v3.0.0+](https://github.com/kubernetes-csi/external-provisioner/releases/tag/v3.0.0)
* [csi-attacher:v3.3.0+](https://github.com/kubernetes-csi/external-attacher/releases/tag/v3.3.0)
* [csi-resizer:v1.3.0+](https://github.com/kubernetes-csi/external-resizer/releases/tag/v1.3.0)

In the CLI, the access modes are abbreviated to:

* RWO - ReadWriteOnce
* ROX - ReadOnlyMany
* RWX - ReadWriteMany
* RWOP - ReadWriteOncePod

#### Note:

Kubernetes uses volume access modes to match PersistentVolumeClaims and PersistentVolumes.
In some cases, the volume access modes also constrain where the PersistentVolume can be mounted.
Volume access modes do **not** enforce write protection once the storage has been mounted.
Even if the access modes are specified as ReadWriteOnce, ReadOnlyMany, or ReadWriteMany,
they don't set any constraints on the volume. For example, even if a PersistentVolume is
created as ReadOnlyMany, it is no guarantee that it will be read-only. If the access modes
are specified as ReadWriteOncePod, the volume is constrained and can be mounted on only a single Pod.

> **Important!** A volume can only be mounted using one access mode at a time,
> even if it supports many.

| Volume Plugin | ReadWriteOnce | ReadOnlyMany | ReadWriteMany | ReadWriteOncePod |
| --- | --- | --- | --- | --- |
| AzureFile | ✓ | ✓ | ✓ | - |
| CephFS | ✓ | ✓ | ✓ | - |
| CSI | depends on the driver | depends on the driver | depends on the driver | depends on the driver |
| FC | ✓ | ✓ | - | - |
| FlexVolume | ✓ | ✓ | depends on the driver | - |
| HostPath | ✓ | - | - | - |
| iSCSI | ✓ | ✓ | - | - |
| NFS | ✓ | ✓ | ✓ | - |
| RBD | ✓ | ✓ | - | - |
| VsphereVolume | ✓ | - | - (works when Pods are collocated) | - |
| PortworxVolume | ✓ | - | ✓ | - |

### Class

A PV can have a class, which is specified by setting the
`storageClassName` attribute to the name of a
[StorageClass](/docs/concepts/storage/storage-classes/).
A PV of a particular class can only be bound to PVCs requesting
that class. A PV with no `storageClassName` has no class and can only be bound
to PVCs that request no particular class.

In the past, the annotation `volume.beta.kubernetes.io/storage-class` was used instead
of the `storageClassName` attribute. This annotation is still working; however,
it will become fully deprecated in a future Kubernetes release.

### Reclaim Policy

Current reclaim policies are:

* Retain -- manual reclamation
* Recycle -- basic scrub (`rm -rf /thevolume/*`)
* Delete -- delete the volume

For Kubernetes 1.36, only `nfs` and `hostPath` volume types support recycling.

### Mount Options

A Kubernetes administrator can specify additional mount options for when a
Persistent Volume is mounted on a node.

#### Note:

Not all Persistent Volume types support mount options.

The following volume types support mount options:

* `csi` (including CSI migrated volume types)
* `iscsi`
* `nfs`

Mount options are not validated. If a mount option is invalid, the mount fails.

In the past, the annotation `volume.beta.kubernetes.io/mount-options` was used instead
of the `mountOptions` attribute. This annotation is still working; however,
it will become fully deprecated in a future Kubernetes release.

### Node Affinity

#### Note:

For most volume types, you do not need to set this field.
You need to explicitly set this for [local](/docs/concepts/storage/volumes/#local) volumes.

A PV can specify node affinity to define constraints that limit what nodes this
volume can be accessed from. Pods that use a PV will only be scheduled to nodes
that are selected by the node affinity. To specify node affinity, set
`nodeAffinity` in the `.spec` of a PV. The
[PersistentVolume](/docs/reference/kubernetes-api/config-and-storage-resources/persistent-volume-v1/#PersistentVolumeSpec)
API reference has more details on this field.

#### Updates to node affinity

FEATURE STATE:
`Kubernetes v1.35 [alpha]`(disabled by default)

If the `MutablePVNodeAffinity` [feature gate](/docs/reference/command-line-tools-reference/feature-gates/) is enabled in your cluster,
the `.spec.nodeAffinity` field of a PersistentVolume is mutable.
This allows cluster administrators or external storage controller to update the node affinity of a PersistentVolume when the data is migrated,
without interrupting the running pods.

When updating the node affinity, you should ensure that the new node affinity still matches the nodes where the volume is currently in use.
For the pods violating the new affinity, if the pod is already running, it may continue to run. But Kubernetes does not support this configuration.
You should terminate the violating pods soon.
Due to in memory caching, the pods created after the update may still be scheduled according to the old node affinity for a short period of time.

To use this feature, you should enable the `MutablePVNodeAffinity` feature gate on the following components:

* `kube-apiserver`
* `kubelet`

### Phase

A PersistentVolume will be in one of the following phases:

`Available`
:   a free resource that is not yet bound to a claim

`Bound`
:   the volume is bound to a claim

`Released`
:   the claim has been deleted, but the associated storage resource is not yet reclaimed by the cluster

`Failed`
:   the volume has failed its (automated) reclamation

You can see the name of the PVC bound to the PV using `kubectl describe persistentvolume <name>`.

#### Phase transition timestamp

FEATURE STATE:
`Kubernetes v1.31 [stable]`(enabled by default)

The `.status` field for a PersistentVolume can include an alpha `lastPhaseTransitionTime` field. This field records
the timestamp of when the volume last transitioned its phase. For newly created
volumes the phase is set to `Pending` and `lastPhaseTransitionTime` is set to
the current time.

## PersistentVolumeClaims

Each PVC contains a spec and status, which is the specification and status of the claim.
The name of a PersistentVolumeClaim object must be a valid
[DNS subdomain name](/docs/concepts/overview/working-with-objects/names/#dns-subdomain-names).

```
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: myclaim
spec:
  accessModes:
    - ReadWriteOnce
  volumeMode: Filesystem
  resources:
    requests:
      storage: 8Gi
  storageClassName: slow
  selector:
    matchLabels:
      release: "stable"
    matchExpressions:
      - {key: environment, operator: In, values: [dev]}
```

### Access Modes

Claims use [the same conventions as volumes](#access-modes) when requesting
storage with specific access modes.

### Volume Modes

Claims use [the same convention as volumes](#volume-mode) to indicate the
consumption of the volume as either a filesystem or block device.

### Volume Name

Claims can use the `volumeName` field to explicitly bind to a specific PersistentVolume. You can also leave
`volumeName` unset, indicating that you'd like Kubernetes to set up a new PersistentVolume
that matches the claim.
If the specified PV is already bound to another PVC, the binding will be stuck
in a pending state.

### Resources

Claims, like Pods, can request specific quantities of a resource. In this case,
the request is for storage. The same
[resource model](https://git.k8s.io/design-proposals-archive/scheduling/resources.md)
applies to both volumes and claims.

#### Note:

For `Filesystem` volumes, the storage request refers to the "outer" volume size
(i.e. the allocated size from the storage backend).
This means that the writeable size may be slightly lower for providers that
build a filesystem on top of a block device, due to filesystem overhead.
This is especially visible with XFS, where many metadata features are enabled by default.

### Selector

Claims can specify a
[label selector](/docs/concepts/overview/working-with-objects/labels/#label-selectors)
to further filter the set of volumes.
Only the volumes whose labels match the selector can be bound to the claim.
The selector can consist of two fields:

* `matchLabels` - the volume must have a label with this value
* `matchExpressions` - a list of requirements made by specifying key, list of values,
  and operator that relates the key and values.
  Valid operators include `In`, `NotIn`, `Exists`, and `DoesNotExist`.

All of the requirements, from both `matchLabels` and `matchExpressions`, are
ANDed together – they must all be satisfied in order to match.

### Class

A claim can request a particular class by specifying the name of a
[StorageClass](/docs/concepts/storage/storage-classes/)
using the attribute `storageClassName`.
Only PVs of the requested class, ones with the same `storageClassName` as the PVC,
can be bound to the PVC.

PVCs don't necessarily have to request a class. A PVC with its `storageClassName` set
equal to `""` is always interpreted to be requesting a PV with no class, so it
can only be bound to PVs with no class (no annotation or one set equal to `""`).
A PVC with no `storageClassName` is not quite the same and is treated differently
by the cluster, depending on whether the
[`DefaultStorageClass` admission plugin](/docs/reference/access-authn-authz/admission-controllers/#defaultstorageclass)
is turned on.

* If the admission plugin is turned on, the administrator may specify a default StorageClass.
  All PVCs that have no `storageClassName` can be bound only to PVs of that default.
  Specifying a default StorageClass is done by setting the annotation
  `storageclass.kubernetes.io/is-default-class` equal to `true` in a StorageClass object.
  If the administrator does not specify a default, the cluster responds to PVC creation
  as if the admission plugin were turned off.
  If more than one default StorageClass is specified, the newest default is used when
  the PVC is dynamically provisioned.
* If the admission plugin is turned off, there is no notion of a default StorageClass.
  All PVCs that have `storageClassName` set to `""` can be bound only to PVs
  that have `storageClassName` also set to `""`.
  However, PVCs with missing `storageClassName` can be updated later once default StorageClass becomes available.
  If the PVC gets updated it will no longer bind to PVs that have `storageClassName` also set to `""`.

See [retroactive default StorageClass assignment](#retroactive-default-storageclass-assignment) for more details.

Depending on installation method, a default StorageClass may be deployed
to a Kubernetes cluster by addon manager during installation.

When a PVC specifies a `selector` in addition to requesting a StorageClass,
the requirements are ANDed together: only a PV of the requested class and with
the requested labels may be bound to the PVC.

#### Note:

Currently, a PVC with a non-empty `selector` can't have a PV dynamically provisioned for it.

In the past, the annotation `volume.beta.kubernetes.io/storage-class` was used instead
of `storageClassName` attribute. This annotation is still working; however,
it won't be supported in a future Kubernetes release.

#### Retroactive default StorageClass assignment

FEATURE STATE:
`Kubernetes v1.28 [stable]`

You can create a PersistentVolumeClaim without specifying a `storageClassName`
for the new PVC, and you can do so even when no default StorageClass exists
in your cluster. In this case, the new PVC creates as you defined it, and the
`storageClassName` of that PVC remains unset until default becomes available.

When a default StorageClass becomes available, the control plane identifies any
existing PVCs without `storageClassName`. For the PVCs that either have an empty
value for `storageClassName` or do not have this key, the control plane then
updates those PVCs to set `storageClassName` to match the new default StorageClass.
If you have an existing PVC where the `storageClassName` is `""`, and you configure
a default StorageClass, then this PVC will not get updated.

In order to keep binding to PVs with `storageClassName` set to `""`
(while a default StorageClass is present), you need to set the `storageClassName`
of the associated PVC to `""`.

This behavior helps administrators change default StorageClass by removing the
old one first and then creating or setting another one. This brief window while
there is no default causes PVCs without `storageClassName` created at that time
to not have any default, but due to the retroactive default StorageClass
assignment this way of changing defaults is safe.

### Unused PVC tracking

FEATURE STATE:
`Kubernetes v1.36 [alpha]`(disabled by default)

When enabled, the PVC protection controller adds an `Unused`
[condition](/docs/concepts/workloads/pods/pod-lifecycle/#pod-conditions) to each
PersistentVolumeClaim to indicate whether it is currently referenced by any
non-terminal Pod.

The condition has two states:

`Unused` with status `"True"` (reason `NoPodsUsingPVC`)
:   No non-terminal Pod references this PVC. The `lastTransitionTime` records when
    the PVC became unused.

`Unused` with status `"False"` (reason `PodUsingPVC`)
:   At least one non-terminal Pod currently references this PVC. The
    `lastTransitionTime` records when the PVC started being used.

A Pod is considered non-terminal if its phase is not `Succeeded` or `Failed`.
This means that a Pending Pod (even one that has not yet been scheduled) counts
as using the PVC.

The `lastTransitionTime` of the `Unused` condition can be used by cluster
administrators, monitoring tools, and external controllers to identify PVCs that
have been unused for a long time. For example, to find all PVCs that have been
unused for more than 30 days, you could query for PVCs where the `Unused`
condition has `status: "True"` and `lastTransitionTime` is older than 30 days.

#### Note:

The unused duration indicated by this condition may be shorter than the actual
unused time because of processing delays in the controller or because the
feature was enabled after the PVC was already unused. The condition is not
updated when a PVC has `deletionTimestamp` set (that is, PVCs that are being deleted).

## Claims As Volumes

Pods access storage by using the claim as a volume. Claims must exist in the
same namespace as the Pod using the claim. The cluster finds the claim in the
Pod's namespace and uses it to get the PersistentVolume backing the claim.
The volume is then mounted to the host and into the Pod.

```
apiVersion: v1
kind: Pod
metadata:
  name: mypod
spec:
  containers:
    - name: myfrontend
      image: nginx
      volumeMounts:
      - mountPath: "/var/www/html"
        name: mypd
  volumes:
    - name: mypd
      persistentVolumeClaim:
        claimName: myclaim
```

### A Note on Namespaces

PersistentVolumes binds are exclusive, and since PersistentVolumeClaims are
namespaced objects, mounting claims with "Many" modes (`ROX`, `RWX`) is only
possible within one namespace.

### PersistentVolumes typed `hostPath`

A `hostPath` PersistentVolume uses a file or directory on the Node to emulate
network-attached storage. See
[an example of `hostPath` typed volume](/docs/tutorials/configuration/configure-persistent-volume-storage/#create-a-persistentvolume).

## Raw Block Volume Support

FEATURE STATE:
`Kubernetes v1.18 [stable]`

The following volume plugins support raw block volumes, including dynamic provisioning where
applicable:

* CSI (including some CSI migrated volume types)
* FC (Fibre Channel)
* iSCSI
* Local volume

### PersistentVolume using a Raw Block Volume

```
apiVersion: v1
kind: PersistentVolume
metadata:
  name: block-pv
spec:
  capacity:
    storage: 10Gi
  accessModes:
    - ReadWriteOnce
  volumeMode: Block
  persistentVolumeReclaimPolicy: Retain
  fc:
    targetWWNs: ["50060e801049cfd1"]
    lun: 0
    readOnly: false
```

### PersistentVolumeClaim requesting a Raw Block Volume

```
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: block-pvc
spec:
  accessModes:
    - ReadWriteOnce
  volumeMode: Block
  resources:
    requests:
      storage: 10Gi
```

### Pod specification adding Raw Block Device path in container

```
apiVersion: v1
kind: Pod
metadata:
  name: pod-with-block-volume
spec:
  containers:
    - name: fc-container
      image: fedora:26
      command: ["/bin/sh", "-c"]
      args: [ "tail -f /dev/null" ]
      volumeDevices:
        - name: data
          devicePath: /dev/xvda
  volumes:
    - name: data
      persistentVolumeClaim:
        claimName: block-pvc
```

#### Note:

When adding a raw block device for a Pod, you specify the device path in the
container instead of a mount path.

### Binding Block Volumes

If a user requests a raw block volume by indicating this using the `volumeMode`
field in the PersistentVolumeClaim spec, the binding rules differ slightly from
previous releases that didn't consider this mode as part of the spec.
Listed is a table of possible combinations the user and admin might specify for
requesting a raw block device. The table indicates if the volume will be bound or
not given the combinations: Volume binding matrix for statically provisioned volumes:

| PV volumeMode | PVC volumeMode | Result |
| --- | --- | --- |
| unspecified | unspecified | BIND |
| unspecified | Block | NO BIND |
| unspecified | Filesystem | BIND |
| Block | unspecified | NO BIND |
| Block | Block | BIND |
| Block | Filesystem | NO BIND |
| Filesystem | Filesystem | BIND |
| Filesystem | Block | NO BIND |
| Filesystem | unspecified | BIND |

#### Note:

Only statically provisioned volumes are supported for alpha release. Administrators
should take care to consider these values when working with raw block devices.

## Volume Snapshot and Restore Volume from Snapshot Support

FEATURE STATE:
`Kubernetes v1.20 [stable]`

Volume snapshots only support the out-of-tree CSI volume plugins.
For details, see [Volume Snapshots](/docs/concepts/storage/volume-snapshots/).
In-tree volume plugins are deprecated. You can read about the deprecated volume
plugins in the
[Volume Plugin FAQ](https://github.com/kubernetes/community/blob/main/sig-storage/volume-plugin-faq.md).

### Create a PersistentVolumeClaim from a Volume Snapshot

```
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: restore-pvc
spec:
  storageClassName: csi-hostpath-sc
  dataSource:
    name: new-snapshot-test
    kind: VolumeSnapshot
    apiGroup: snapshot.storage.k8s.io
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 10Gi
```

## Volume Cloning

[Volume Cloning](/docs/concepts/storage/volume-pvc-datasource/)
only available for CSI volume plugins.

### Create PersistentVolumeClaim from an existing PVC

```
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: cloned-pvc
spec:
  storageClassName: my-csi-plugin
  dataSource:
    name: existing-src-pvc-name
    kind: PersistentVolumeClaim
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 10Gi
```

## Volume populators and data sources

FEATURE STATE:
`Kubernetes v1.24 [beta]`

Kubernetes supports custom volume populators.
To use custom volume populators, you must enable the `AnyVolumeDataSource`
[feature gate](/docs/reference/command-line-tools-reference/feature-gates/) for
the kube-apiserver and kube-controller-manager.

Volume populators take advantage of a PVC spec field called `dataSourceRef`. Unlike the
`dataSource` field, which can only contain either a reference to another PersistentVolumeClaim
or to a VolumeSnapshot, the `dataSourceRef` field can contain a reference to any object in the
same namespace, except for core objects other than PVCs. For clusters that have the feature
gate enabled, use of the `dataSourceRef` is preferred over `dataSource`.

## Cross namespace data sources

FEATURE STATE:
`Kubernetes v1.26 [alpha]`

Kubernetes supports cross namespace volume data sources.
To use cross namespace volume data sources, you must enable the `AnyVolumeDataSource`
and `CrossNamespaceVolumeDataSource`
[feature gates](/docs/reference/command-line-tools-reference/feature-gates/) for
the kube-apiserver and kube-controller-manager.
Also, you must enable the `CrossNamespaceVolumeDataSource` feature gate for the csi-provisioner.

Enabling the `CrossNamespaceVolumeDataSource` feature gate allows you to specify
a namespace in the dataSourceRef field.

#### Note:

When you specify a namespace for a volume data source, Kubernetes checks for a
ReferenceGrant in the other namespace before accepting the reference.
ReferenceGrant is part of the `gateway.networking.k8s.io` extension APIs.
See [ReferenceGrant](https://gateway-api.sigs.k8s.io/api-types/referencegrant/)
in the Gateway API documentation for details.
This means that you must extend your Kubernetes cluster with at least ReferenceGrant from the
Gateway API before you can use this mechanism.

## Data source references

The `dataSourceRef` field behaves almost the same as the `dataSource` field. If one is
specified while the other is not, the API server will give both fields the same value. Neither
field can be changed after creation, and attempting to specify different values for the two
fields will result in a validation error. Therefore the two fields will always have the same
contents.

There are two differences between the `dataSourceRef` field and the `dataSource` field that
users should be aware of:

* The `dataSource` field ignores invalid values (as if the field was blank) while the
  `dataSourceRef` field never ignores values and will cause an error if an invalid value is
  used. Invalid values are any core object (objects with no apiGroup) except for PVCs.
* The `dataSourceRef` field may contain different types of objects, while the `dataSource` field
  only allows PVCs and VolumeSnapshots.

When the `CrossNamespaceVolumeDataSource` feature is enabled, there are additional differences:

* The `dataSource` field only allows local objects, while the `dataSourceRef` field allows
  objects in any namespaces.
* When namespace is specified, `dataSource` and `dataSourceRef` are not synced.

Users should always use `dataSourceRef` on clusters that have the feature gate enabled, and
fall back to `dataSource` on clusters that do not. It is not necessary to look at both fields
under any circumstance. The duplicated values with slightly different semantics exist only for
backwards compatibility. In particular, a mixture of older and newer controllers are able to
interoperate because the fields are the same.

### Using volume populators

Volume populators are [controllers](/docs/concepts/architecture/controller/ "A control loop that watches the shared state of the cluster through the apiserver and makes changes attempting to move the current state towards the desired state.") that can
create non-empty volumes, where the contents of the volume are determined by a Custom Resource.
Users create a populated volume by referring to a Custom Resource using the `dataSourceRef` field:

```
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: populated-pvc
spec:
  dataSourceRef:
    name: example-name
    kind: ExampleDataSource
    apiGroup: example.storage.k8s.io
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 10Gi
```

Because volume populators are external components, attempts to create a PVC that uses one
can fail if not all the correct components are installed. External controllers should generate
events on the PVC to provide feedback on the status of the creation, including warnings if
the PVC cannot be created due to some missing component.

You can install the alpha [volume data source validator](https://github.com/kubernetes-csi/volume-data-source-validator)
controller into your cluster. That controller generates warning Events on a PVC in the case that no populator
is registered to handle that kind of data source. When a suitable populator is installed for a PVC, it's the
responsibility of that populator controller to report Events that relate to volume creation and issues during
the process.

### Using a cross-namespace volume data source

FEATURE STATE:
`Kubernetes v1.26 [alpha]`

Create a ReferenceGrant to allow the namespace owner to accept the reference.
You define a populated volume by specifying a cross namespace volume data source
using the `dataSourceRef` field. You must already have a valid ReferenceGrant
in the source namespace:

```
apiVersion: gateway.networking.k8s.io/v1beta1
kind: ReferenceGrant
metadata:
  name: allow-ns1-pvc
  namespace: default
spec:
  from:
  - group: ""
    kind: PersistentVolumeClaim
    namespace: ns1
  to:
  - group: snapshot.storage.k8s.io
    kind: VolumeSnapshot
    name: new-snapshot-demo
```

```
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: foo-pvc
  namespace: ns1
spec:
  storageClassName: example
  accessModes:
  - ReadWriteOnce
  resources:
    requests:
      storage: 1Gi
  dataSourceRef:
    apiGroup: snapshot.storage.k8s.io
    kind: VolumeSnapshot
    name: new-snapshot-demo
    namespace: default
  volumeMode: Filesystem
```

## Writing Portable Configuration

If you're writing configuration templates or examples that run on a wide range of clusters
and need persistent storage, it is recommended that you use the following pattern:

* Include PersistentVolumeClaim objects in your bundle of config (alongside
  Deployments, ConfigMaps, etc).
* Do not include PersistentVolume objects in the config, since the user instantiating
  the config may not have permission to create PersistentVolumes.
* Give the user the option of providing a storage class name when instantiating
  the template.
  + If the user provides a storage class name, put that value into the
    `persistentVolumeClaim.storageClassName` field.
    This will cause the PVC to match the right storage
    class if the cluster has StorageClasses enabled by the admin.
  + If the user does not provide a storage class name, leave the
    `persistentVolumeClaim.storageClassName` field as nil. This will cause a
    PV to be automatically provisioned for the user with the default StorageClass
    in the cluster. Many cluster environments have a default StorageClass installed,
    or administrators can create their own default StorageClass.
* In your tooling, watch for PVCs that are not getting bound after some time
  and surface this to the user, as this may indicate that the cluster has no
  dynamic storage support (in which case the user should create a matching PV)
  or the cluster has no storage system (in which case the user cannot deploy
  config requiring PVCs).

## What's next

* Learn more about [Creating a PersistentVolume](/docs/tutorials/configuration/configure-persistent-volume-storage/#create-a-persistentvolume).
* Learn more about [Creating a PersistentVolumeClaim](/docs/tutorials/configuration/configure-persistent-volume-storage/#create-a-persistentvolumeclaim).
* Read the [Persistent Storage design document](https://git.k8s.io/design-proposals-archive/storage/persistent-storage.md).

### API references

Read about the APIs described in this page:

* [`PersistentVolume`](/docs/reference/kubernetes-api/config-and-storage-resources/persistent-volume-v1/)
* [`PersistentVolumeClaim`](/docs/reference/kubernetes-api/config-and-storage-resources/persistent-volume-claim-v1/)

## Feedback

Was this page helpful?

Yes
No

Thanks for the feedback. If you have a specific, answerable question about how to use Kubernetes, ask it on
[Stack Overflow](https://stackoverflow.com/questions/tagged/kubernetes).
Open an issue in the [GitHub Repository](https://www.github.com/kubernetes/website/) if you want to
[report a problem](https://github.com/kubernetes/website/issues/new?title=Issue%20with%20k8s.io)
or
[suggest an improvement](https://github.com/kubernetes/website/issues/new?title=Improvement%20for%20k8s.io).

  

Last modified April 14, 2026 at 1:15 AM PST: [fix(links): update kubernetes/community links from master to main (03c191bcc4)](https://github.com/kubernetes/website/commit/03c191bcc446f9c15a9e68d6cd1154b53bde4291)

© 2026 The Kubernetes Authors | Documentation Distributed under [CC BY 4.0](https://git.k8s.io/website/LICENSE)

© 2026 The Linux Foundation ®. All rights reserved. The Linux Foundation has registered trademarks and uses trademarks. For a list of trademarks of The Linux Foundation, please see our [Trademark Usage page](https://www.linuxfoundation.org/trademark-usage)

ICP license: 京ICP备17074266号-3